"""Test parsing."""
import asyncio
import logging
from pathlib import Path
from typing import Set
from collections import defaultdict
import csv

import aiofiles  # type: ignore
from aiohttp import (ClientConnectorError, ClientOSError, ClientSession,
                     ClientTimeout, ServerTimeoutError)
from bs4 import BeautifulSoup, Tag, NavigableString  # type: ignore  # noqa

OUT_PATH = Path(__file__).parent
OUT_PATH.mkdir(exist_ok=True, parents=True)
OUT_PATH = OUT_PATH.absolute()
FILE_PATH = OUT_PATH / "beasts.csv"

logger = logging.getLogger(__name__)


START_URL = "https://ru.wikipedia.org"
KEY_TYPE_INDEX = 0
LETTER = 1
WRITE_ONLY_ONE_COROUTINE = 1
KEY_NEXT_URL_PARAMS = 0


async def crawl_url(
        session: ClientSession,
        url: str,
        visited: Set[str],
        count_types_animal: dict[str, int],
):
    """Формируем ссылки."""
    if url in visited:
        return

    try:
        resource = await  session.get(url)
        visited.add(url)
        if resource.status != 200:
            logger.warning("Неудачный запрос. Статус код: %s", resource.status)
            return

        result: bytes = await resource.read()

        soup = BeautifulSoup(result, "lxml")

        category_block = soup.find("div", class_="mw-category mw-category-columns", )

        if category_block and isinstance(category_block, Tag):
            animals_data = category_block.find("div", class_="mw-category-group")

            if animals_data:
                async with asyncio.Semaphore(WRITE_ONLY_ONE_COROUTINE):
                    animals: str = animals_data.get_text()
                    animals_list: list[str] = animals.split("\n")
                    if len(animals_list[KEY_TYPE_INDEX]) == LETTER:
                        count_types_animal[animals_list[KEY_TYPE_INDEX]] += len(animals_list) - LETTER
                    else:
                        count_types_animal[animals_list[KEY_TYPE_INDEX][LETTER]] += len(animals_list)

        else:
            logger.debug("Блок не найден")
            return

        next_url_params: None | str | list[str] = None

        next_data_of_link = soup.find("a", string="Следующая страница")


        if next_data_of_link is not None and isinstance(next_data_of_link, Tag):
            next_url_params = next_data_of_link.attrs.get("href")

        else:
            next_data_of_link = soup.find(
                "a", attrs={"title": "Категория:Животные по алфавиту"}
            )

            if next_data_of_link is not None and isinstance(next_data_of_link, Tag):
                next_url_params = next_data_of_link.get("href")




        if next_url_params and isinstance(next_url_params, list) and len(next_url_params) > 0:
            next_url_params.remove(url)
            next_url_params = next_url_params[KEY_NEXT_URL_PARAMS]

        url = f"{START_URL}{next_url_params}"

        del category_block
        del soup

        await crawl_url(session=session,
                      url=url,
                      visited=visited,
                      count_types_animal=count_types_animal,
                      )


    except (ServerTimeoutError, ClientConnectorError, ClientOSError,
            asyncio.TimeoutError, OSError,) as e:

        logger.error(e)
        return




async def main() -> None:
    """Создается сессия и запускается рекурсивный обход"""
    visited: Set[str] = set()
    count_type_of_animals: dict[str, int] = defaultdict(int)
    link: str = f"{START_URL}/wiki/Категория:Животные_по_алфавиту"
    async with ClientSession(
            timeout=ClientTimeout(connect=5, total=10)
    ) as session:
        await crawl_url(
            session=session, url=link, visited=visited,
            count_types_animal=count_type_of_animals,
        )

    letter: str
    count: int

    async with aiofiles.open(FILE_PATH, mode="w", encoding="utf-8", newline="") as f:
        logger.debug("Создание файла: %s", FILE_PATH)
        writer = csv.writer(f)
        await writer.writerow(["Letter", "Count"])
        for letter, count in count_type_of_animals.items():
            await writer.writerow([str(letter), str(count)])

    logger.info("Звери собраны.")



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
