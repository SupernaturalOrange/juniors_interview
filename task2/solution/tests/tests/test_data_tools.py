import pytest

from task2.solution.settings.settings import Settings
from task2.solution.tools.data_tools import (
    convert_set_list_to_dict_counts,
    get_additional_param,
    get_all_animals,
)


@pytest.mark.data_tools
def test_get_additional_param_func() -> None:
    """
    Проверим утилиту, извлекающую параметры из строкового представления url.

    :return: None.
    """
    url = "https://mysite.by/search/?text=Смешные+видео&category=Коты"
    params = get_additional_param(url)

    # Ожидаем этот словарь:
    expected_dictionary = dict(text="Смешные видео", category="Коты")

    assert params == expected_dictionary


@pytest.mark.data_tools
def test_convert_set_list_to_dict_counts_func() -> None:
    """
    Проверим улиту, которая конвертирует список из множеств названий животных,
    где в одном множестве все животные начинаются на одну и ту же букву, в список из словарей.
    В каждом словаре будут ключи "letter" и "count",
    где "letter" - это буква, с которой начинается имя животных в множестве,
    а "count" - количество этих животных в множестве.

    :return: None.
    """
    list_animals = [{"Заяц", "Зебра"}, {"Волк", "Вол", "Варан"}]
    data = convert_set_list_to_dict_counts(list_animals)

    assert isinstance(data, list)
    assert len(data) == 2
    assert all(isinstance(item, dict) for item in data)

    for item in data:
        assert isinstance(item["count"], int)
        assert isinstance(item["letter"], str)

        assert "З" in item["letter"] or "В" in item["letter"]
        assert item["count"] == 2 or item["count"] == 3


@pytest.mark.data_tools
def test_get_all_animals_func(settings: Settings) -> None:
    """
    Проверим функцию get_all_animals.
    Передав в неё файл настроек и букву, на которую должны начинаться названия животных,
    должны получить все имена животных.

    :param settings: Изменённые настройки для приложения.
    :return: None.
    """
    animals_set = get_all_animals(settings, "Б")

    assert isinstance(animals_set, set)
    assert len(animals_set) > 0
    assert all(isinstance(name, str) for name in animals_set)
    assert all(name.startswith("Б") for name in animals_set)
