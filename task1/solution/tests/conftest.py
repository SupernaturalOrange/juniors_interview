from typing import Any, Callable, ParamSpec, TypeVar

import pytest
from tests.functions.functions import area_of_the_rectangle, sum_two_int_numbers
from tools.decorators.decorators import strict

T = TypeVar("T")
P = ParamSpec("P")


@pytest.fixture
def func_sum_two_int_numbers() -> Callable[[Any, Any], Any]:
    return sum_two_int_numbers


@pytest.fixture
def func_area_of_the_rectangle() -> Callable[[Any, Any], Any]:
    return area_of_the_rectangle


@pytest.fixture
def decorator_strict() -> Callable[[Callable[P, T]], Callable[P, T]]:
    return strict
