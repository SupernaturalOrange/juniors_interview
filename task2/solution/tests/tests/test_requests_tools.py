import pytest

from task2.solution.settings.settings import Settings
from task2.solution.tools.bs_tools import get_all_animals_on_page, get_link_next_page
from task2.solution.tools.requests_tools import get_response_with_settings


@pytest.mark.requests_tools
def test_get_response_with_settings_func(settings: Settings) -> None:
    """
    Тестируем функцию get_response_with_settings.
    Ожидаем статус 200. Бонусом проверим, что на странице есть то, что ожидаем.

    :param settings: Изменённые настройки для приложения.
    :return: None.
    """
    additional_param = {"from": "А"}
    response = get_response_with_settings(settings, additional_param)
    assert response.status_code == 200

    # Проверим, есть ли на странице ссылка на следующую страницу
    link = get_link_next_page(response.text)
    assert isinstance(link, str)

    # Проверим, что на странице есть животные на букву А
    next_page, animals_set = get_all_animals_on_page(response.text, "А")
    assert next_page is True
    assert isinstance(animals_set, set)

    # тут опционально, так как на момент написания тестов на странице показывало по 200 животных.
    assert len(animals_set) == 200
    assert all(name.startswith("А") for name in animals_set)
