from urllib.parse import unquote

import pytest

from task2.solution.tools.bs_tools import get_all_animals_on_page, get_link_next_page


@pytest.mark.bs_tools
def test_get_link_next_page_func(no_next_page: str) -> None:
    """
    Тестируем функцию get_link_next_page.
    Наша задача убедиться, что функция на странице находит ссылку.

    :param no_next_page: Страница поиска. Будем рассматривать страницу no_next_page,
        так как мы заранее знаем, что должны найти.
    :return: None
    """
    link_next_page = get_link_next_page(no_next_page)
    assert link_next_page is not None

    # Так как это сохранённая страница, то параметры нужной ссылки известны:
    url = unquote(link_next_page)
    assert "https://ru.wikipedia.org/" in url
    assert "title=Категория:Животные_по_алфавиту" in url
    assert "from=Эквадорский+чёрный+кассик" in url


@pytest.mark.bs_tools
def test_get_all_animals_on_page_func_next_page_false(no_next_page: str) -> None:
    """
    Тестируем функцию get_all_animals_on_page.
    Наша задача убедиться, что функция на странице находит всех животных, которые начинаются на определённую букву.
    Данный тест предполагает, что функция вернёт вместе с множеством животных объект False,
    так как на странице есть животные, которые начинаются уже на другую букву.

    :param no_next_page: Страница, где животные начинаются с разных букв.
    :return: None
    """

    next_page, animals_set = get_all_animals_on_page(no_next_page, "Щ")

    assert next_page is False
    assert isinstance(animals_set, set)
    assert len(animals_set) == 160


@pytest.mark.bs_tools
def test_get_all_animals_on_page_func_next_page_true(yes_next_page: str) -> None:
    """
    Тестируем функцию get_all_animals_on_page.
    Наша задача убедиться, что функция на странице находит всех животных, которые начинаются на определённую букву.
    Данный тест предполагает, что функция вернёт вместе с множеством животных объект True,
    так как на странице все животные начинаются на одну и ту же букву.

    :param yes_next_page: Страница, где животные начинаются с одинаковой буквы.
    :return: None
    """

    next_page, animals_set = get_all_animals_on_page(yes_next_page, "А")

    assert next_page is True
    assert isinstance(animals_set, set)
    assert len(animals_set) == 200
