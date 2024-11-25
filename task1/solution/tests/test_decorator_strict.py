from typing import Any, ParamSpec, TypeVar

import pytest

T = TypeVar("T")
P = ParamSpec("P")


def test_decorator_strict_with_func_sum_two_int_numbers(
    func_sum_two_int_numbers: Any,
    decorator_strict: Any,
) -> None:
    """
    Тест декоратора strict с функцией, которая принимает на себя два целых числа и возвращает их сумму.
    :param func_sum_two_int_numbers: Тестируемая функция.
    :param decorator_strict: Тестируемый декоратор.
    :return: None.
    """

    # Наша тестируемая функция хоть и должна слаживать только целые числа,
    # но без декоратора она сложит и float и даже str, проверим это перед тестом декоратора:
    a_float = 1.5
    b_float = 3.5
    assert func_sum_two_int_numbers(a_float, b_float) == (a_float + b_float)

    a_str = "a"
    b_str = "b"
    assert func_sum_two_int_numbers(a_str, b_str) == (a_str + b_str)

    a_int = 1
    b_int = 3
    assert func_sum_two_int_numbers(a_int, b_int) == (a_int + b_int)

    # Теперь приступим к тесту декоратора.
    decor_func = decorator_strict(func_sum_two_int_numbers)

    # Ниже ожидаем исключение TypeError, иначе тесты упадут.
    with pytest.raises(TypeError):
        decor_func(a_float, b_float)

    with pytest.raises(TypeError):
        decor_func(a_str, b_str)

    # Но не возникнет ошибки, если переданные аргументы верные.
    assert decor_func(a_int, b_int) == (a_int + b_int)


def test_decorator_strict_with_func_area_of_the_rectangle(
    func_area_of_the_rectangle: Any,
    decorator_strict: Any,
) -> None:
    """
    Тест декоратора strict с функцией, которая принимает на себя два числа с плавающей точкой и умножает их.
    :param func_area_of_the_rectangle: Тестируемая функция.
    :param decorator_strict: Тестируемый декоратор.
    :return: None.
    """

    # Проверим, что функция без декоратора посчитает нам как целые числа, так и числа с плавающей точкой.
    a_float = 1.5
    b_float = 3.5
    assert func_area_of_the_rectangle(a_float, b_float) == (a_float * b_float)

    a_int = 1
    b_int = 3
    assert func_area_of_the_rectangle(a_int, b_int) == (a_int * b_int)

    # Теперь приступим к тесту декоратора.
    decor_func = decorator_strict(func_area_of_the_rectangle)

    # Ниже ожидаем исключение TypeError, иначе тесты упадут.
    with pytest.raises(TypeError):
        decor_func(a_int, b_int)

    # Но не возникнет ошибки, если переданные аргументы верные.
    assert decor_func(a_float, b_float) == (a_float * b_float)
