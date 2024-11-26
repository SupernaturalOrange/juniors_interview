from typing import Any, Callable, ParamSpec, TypeVar

import pytest

from task1.solution.tools.decorators.decorators import strict

from .functions.functions import area_of_the_rectangle, sum_two_int_numbers

T = TypeVar("T")
P = ParamSpec("P")


@pytest.fixture
def func_sum_two_int_numbers() -> Callable[[Any, Any], Any]:
    """
    Pytest фикстура, возвращает ссылку на функцию сложения двух объектов.

    :return: Ссылку на функцию сложения двух объектов.
    """
    return sum_two_int_numbers


@pytest.fixture
def func_area_of_the_rectangle() -> Callable[[Any, Any], Any]:
    """
    Pytest фикстура, возвращает ссылку на функцию умножения двух объектов.

    :return: Ссылку на функцию умножения двух объектов
    """
    return area_of_the_rectangle


@pytest.fixture
def decorator_strict() -> Callable[[Callable[P, T]], Callable[P, T]]:
    """
    Pytest фикстура, возвращает ссылку на тестируемый декоратор.

    :return: Ссылку на тестируемый декоратор
    """
    return strict
