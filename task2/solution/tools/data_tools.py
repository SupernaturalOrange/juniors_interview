import re
from typing import Dict, List, Set
from urllib.parse import unquote

from task2.solution.settings.settings import Settings
from task2.solution.tools.bs_tools import get_all_animals_on_page, get_link_next_page
from task2.solution.tools.exception_classes import NoParametersInTheLink
from task2.solution.tools.requests_tools import get_response_with_settings


def get_additional_param(url: str) -> Dict[str, str]:
    """
    Функция извлекает из строковой url query параметры, и возвращает их в качестве словаря.

    :param url: Url.
    :return: Словарь.
    """
    url = unquote(url)
    pattern = r"[?&]{1}([^?&#]+)"
    search_result = re.findall(pattern, url)
    if not search_result:
        raise NoParametersInTheLink(f"Не нашлось параметров в ссылке: {url}")
    return dict(param.replace("+", " ").split("=") for param in search_result)


def __get_all_animals_recursively(
    settings: Settings, additional_param: Dict[str, str], initial_letter: str
) -> Set[str]:
    """
    Функция рекурсивно соберёт все имена животных, пока не встретит животное, имя которого начинается с другой буквы.

    :param settings: Настройки (экземпляр класса Settings).
    :param additional_param: Дополнительные query параметры.
    :param initial_letter: Одна буква, с которой должно начинаться имя животного (str),
        если букв будет больше, то остальные будут игнорироваться.
    :return:
    """
    response = get_response_with_settings(settings, additional_param)
    next_page, animals = get_all_animals_on_page(response.text, initial_letter)
    if next_page:
        link_next_page = get_link_next_page(response.text)
        params = get_additional_param(link_next_page)
        animals.update(__get_all_animals_recursively(settings, params, initial_letter))
    return animals


def get_all_animals(settings: Settings, initial_letter: str) -> Set[str]:
    """
    Функция подготовит и запустит рекурсивную функцию сбора всех имён животных.

    :param settings: Настройки (экземпляр класса Settings).
    :param initial_letter: Одна буква, с которой должно начинаться имя животного (str),
        если букв будет больше, то остальные будут игнорироваться.
    :return: Set из имён животных.
    """
    additional_param = {"from": initial_letter}
    return __get_all_animals_recursively(settings, additional_param, initial_letter)


def convert_set_list_to_dict_counts(
    list_set_animals: List[Set[str]],
) -> List[Dict[str, int | str]]:
    """
    В функцию передаётся список из множеств животных,
    где в каждом множестве все имена животных начинаются с одинаковой буквы.
    Функция конвертирует его в список из словарей,
    где в каждом словаре будут ключи "letter" и "count",
    где "letter" - это буква, с которой начинается имя животных в множестве,
    а "count" - количество этих животных в множестве.

    :param list_set_animals: Список из множеств животных.
    :return: Список из словарей, где ключом будет буква, с которой начинаются имена животных в множестве,
        а значением будет количество этих животных в множестве.
    """
    if not isinstance(list_set_animals, list):
        raise ValueError("Ожидается список из множеств животных.")
    if not list_set_animals:
        raise ValueError("Передаваемый список не может быть пустым")

    statistics_animals_list: List[Dict[str, int | str]] = []
    for animal_set in list_set_animals:
        animal_set.discard("")
        if not isinstance(animal_set, set):
            raise ValueError("Элемент списка должен быть множеством.")
        if not animal_set:
            raise ValueError("Множество не может быть пустым.")
        list_animals = list(animal_set)
        animal: str = list_animals[0]
        animal_start_letter: str = animal[0]
        count_animals: int = len(list_animals)
        statistics_animals_list.append(
            {"letter": animal_start_letter, "count": count_animals}
        )
    return statistics_animals_list
