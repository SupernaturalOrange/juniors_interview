from typing import Set, Tuple

from bs4 import BeautifulSoup, Tag

from task2.solution.tools.exception_classes import NoLinkOnThePage, NoObjectOnThePage


def get_link_next_page(page: str) -> str:
    """
    Функция ищет ссылку на следующую страницу.

    :param page: Текущая страница (str).
    :return: Ссылка на следующую страницу, если она будет найдена, иначе возникнет исключение NoLinkOnThePage.
    """
    soup = BeautifulSoup(page, "html.parser")
    next_page_link = soup.find_all("a", string="Следующая страница")
    if next_page_link:
        next_page_url: str = next_page_link[-1]["href"]
    else:
        raise NoLinkOnThePage(
            "Что-то пошло не так. Не нашлись объекты содержащие фразу 'Следующая страница'."
        )
    return next_page_url


def get_all_animals_on_page(page: str, initial_letter: str) -> Tuple[bool, Set[str]]:
    """
    Функция ищет имена всех животных на странице с заданной начальной буквой.

    :param page: Страница (str).
    :param initial_letter: Одна буква, с которой должно начинаться имя животного (str),
        если букв будет больше, то остальные будут игнорироваться.
    :return: Если не встретятся животные, которые начинаются с другой буквы - вернёт (True, set), иначе (False, set)
    """
    soup = BeautifulSoup(page, "html.parser")
    category_div = soup.find("div", class_="mw-category mw-category-columns")
    if not category_div or not isinstance(category_div, Tag):
        raise NoObjectOnThePage("Не нашлось объекта с перечнем животных")
    animal_links = category_div.find_all("a")
    if not animal_links:
        raise NoObjectOnThePage("Не нашлись объекты с названием животных")
    animals = set()
    next_page = True
    for link in animal_links:
        animal_name = link.text.strip()
        animal_startswith = animal_name.lower().startswith(initial_letter[0].lower())
        if animal_name and animal_startswith:
            animals.add(animal_name)
        elif next_page and not animal_startswith:
            next_page = False
    return next_page, animals
