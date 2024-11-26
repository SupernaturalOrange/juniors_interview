import shutil
from typing import Generator

import pytest

from task2.solution.settings.settings import Settings
from task2.solution.tests.settings import t_settings


@pytest.fixture
def settings() -> Generator[Settings, None, None]:
    """
    Pytest фикстура, возвращает изменённые настройки для приложения.

    :return: Изменённые настройки для приложения.
    """
    yield t_settings

    # Внимание! Тут быть крайне осторожным!
    path = t_settings.base_path / "t_data"
    shutil.rmtree(path, ignore_errors=True)


@pytest.fixture
def no_next_page(settings: Settings) -> str:
    """
    Pytest фикстура, вернёт страницу, где есть животные, которые начинаются на разные буквы.

    :param settings: Изменённые настройки для приложения.
    :return: Страницу, где есть животные, которые начинаются на разные буквы.
    """
    path = settings.base_path / "files" / "no_next.html"
    with open(path, "r") as file:
        page = file.read()
    return page


@pytest.fixture
def yes_next_page(settings: Settings) -> str:
    """
    Pytest фикстура, вернёт страницу, где все животные начинаются с одинаковой буквы.

    :param settings: Изменённые настройки для приложения.
    :return: Страницу, где все животные начинаются с одинаковой буквы.
    """
    path = settings.base_path / "files" / "yes_next.html"
    with open(path, "r") as file:
        page = file.read()
    return page
