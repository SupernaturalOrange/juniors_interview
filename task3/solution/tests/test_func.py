from typing import List

import pytest

from task3.solution.utils.classes import BadTimePoints, PeriodTime
from task3.solution.utils.utils import (
    get_all_intersection,
    normalized_list_period,
    validate_list_time_points,
)


@pytest.mark.parametrize(
    "time_points",
    [
        [1732662986, 1732663102, 1732663126, 1732663116],
        [1732662986, 1732663102, 1732663126],
        [1732662986],
        [],
    ],
)
def test_validate_list_time_points_func_no_valid(time_points: List[int]) -> None:
    """
    Тестируем валидатор списка временных точек.
    Передаём невалидные списки и ожидаем исключение BadTimePoints.

    :return: None.
    """

    with pytest.raises(BadTimePoints):
        validate_list_time_points(time_points)


def test_validate_list_time_points_func_valid() -> None:
    """
    Тестируем валидатор списка временных точек.
    Передадим валидный список, исключения BadTimePoints не должно быть.

    :return: None.
    """
    time_points = [1732662986, 1732663102, 1732663116, 1732663126]
    try:
        validate_list_time_points(time_points)
    except BadTimePoints:
        raise AssertionError()
    else:
        assert True


@pytest.mark.parametrize(
    "time_points",
    [
        [1732662986, 1732663102, 1732663126, 1732663116],
        [1732662986, 1732663102, 1732663126],
        [1732662986],
        [],
    ],
)
def test_normalized_list_period_func_no_valid(time_points: List[int]) -> None:
    """
    Тестируем функцию normalized_list_period.
    Передаём невалидные списки и ожидаем исключение BadTimePoints.

    :return: None.
    """
    with pytest.raises(BadTimePoints):
        normalized_list_period(time_points)


def test_normalized_list_period_func_valid() -> None:
    """
    Тестируем функцию normalized_list_period.
    Передаём валидный список временных точек и ожидаем список из экземпляров класса PeriodTime.

    :return: None.
    """
    time_points = [1732662986, 1732663102, 1732663116, 1732663126]
    periods = normalized_list_period(time_points)

    assert all(isinstance(period, PeriodTime) for period in periods)


def test_class_period_time_get_time() -> None:
    """
    Тестируем класс PeriodTime.
    Проверяем правильно ли он вернёт время в секундах временного отрезка.

    :return: None.
    """
    time_points = (1732664736, 1732664749)
    seconds = time_points[1] - time_points[0]
    period = PeriodTime(time_points)
    assert seconds == period.get_time()


def test_class_period_time_intersection() -> None:
    """
    Тестируем класс PeriodTime.
    Проверяем правильно ли он определяет пересечение отрезков времени.

    :return: None.
    """

    # Зададим отрезки с пересечением в 1 секунду
    time_points_1 = (1732664736, 1732664749)
    period_1 = PeriodTime(time_points_1)

    time_points_2 = (1732664748, 1732664770)
    period_2 = PeriodTime(time_points_2)

    period_intersection_1 = period_1.intersection(period_2)
    assert period_intersection_1 is not None
    assert period_intersection_1.get_time() == 1

    period_intersection_2 = period_2.intersection(period_1)
    assert period_intersection_2 is not None
    assert period_intersection_2.get_time() == 1

    assert period_intersection_1 == period_intersection_2


def test_class_period_time_no_valid_init_data() -> None:
    """
    Тестируем класс PeriodTime.
    Проверим класс с невалидными данными.

    :return: None.
    """
    time_points_1 = (1732664749, 1732664736)
    with pytest.raises(ValueError) as e:
        PeriodTime(time_points_1)
    assert "Начало отрезка времени должно быть меньше конечного" in str(e)

    time_points_2 = (1732664736, 1732664749)
    period = PeriodTime(time_points_2)

    with pytest.raises(ValueError) as e:
        period.time_out = 1732664735
    assert "Начало отрезка времени должно быть меньше конечного" in str(e)

    with pytest.raises(ValueError) as e:
        period.time_in = 1732664750
    assert "Начало отрезка времени должно быть меньше конечного" in str(e)


def test_get_all_intersection_func() -> None:
    """
    Тестируем функцию get_all_intersection.

    :return: None.
    """

    # Создадим временные отрезки
    # Первый большой размером в 30 секунд
    time_points = (1732666610, 1732666640)

    # И 5 поменьше, размерами в 10 секунд,
    # но один заходит слева на 5 секунд, второй внутри, а третий выходит справа на 8 секунд.
    # Остальные где-то слева и справа.
    time_points_1 = (1732666605, 1732666615)
    time_points_2 = (1732666615, 1732666625)
    time_points_3 = (1732666638, 1732666648)

    time_points_4 = (1732666505, 1732666515)
    time_points_5 = (1732666738, 1732666748)

    # Ожидаем временные отрезки длиной 5, 10, 2 секунд соответственно.

    # Преобразуем наши временные отрезки.
    big_period = PeriodTime(time_points)
    small_period_1 = PeriodTime(time_points_1)
    small_period_2 = PeriodTime(time_points_2)
    small_period_3 = PeriodTime(time_points_3)
    small_period_4 = PeriodTime(time_points_4)
    small_period_5 = PeriodTime(time_points_5)

    periods = get_all_intersection(
        big_period,
        [
            small_period_1,
            small_period_2,
            small_period_3,
            small_period_4,
            small_period_5,
        ],
    )
    assert periods is not None
    assert len(periods) == 3
    assert {5, 10, 2} == set(period.get_time() for period in periods)
