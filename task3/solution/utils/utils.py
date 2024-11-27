from typing import List, Optional

from task3.solution.utils.classes import BadTimePoints, PeriodTime


def get_all_intersection(
    period: PeriodTime, list_of_time_periods: List[PeriodTime]
) -> Optional[List[PeriodTime]]:
    """
    Функция определит и вернёт отрезки времени, которые пересекаются с временным отрезком.
    Если пересечений нет - вернёт None.

    :param period: Временной отрезок (PeriodTime).
    :param list_of_time_periods: Список временных отрезков (PeriodTime).
    :return: Список временных отрезков (PeriodTime).
    """
    list_intersection_period = []
    for time_period in list_of_time_periods:
        intersection_period = period.intersection(time_period)
        if intersection_period:
            list_intersection_period.append(intersection_period)
    return list_intersection_period if list_intersection_period else None


def normalized_list_period(time_periods: List[int]) -> List[PeriodTime]:
    """
    Функция преобразует список из временных отметок в список из объектов PeriodTime.
    :param time_periods: Список из временных меток.
    :return: Список из PeriodTime
    """
    validate_list_time_points(time_periods)
    return [PeriodTime(period) for period in zip(time_periods[::2], time_periods[1::2])]


def validate_periods_list(periods: List[PeriodTime]) -> bool:
    """
    Функция проверит, что все отрезки времени в списке не пересекаются.

    :param periods: Список временных отрезков (PeriodTime).
    :return: True, если отрезки не пересекаются, иначе False.
    """
    for i, period in enumerate(periods[1:], 0):
        result = period.intersection(periods[i])
        if result:
            break
    else:
        return True
    return False


def validate_list_time_points(time_points: List[int]) -> None:
    """
    Функция проверит, что все временные точки в списке идут строго по возрастанию,
    их больше 2-х и их чётное количество. В противном случае вызовет исключение BadTimePoints.

    :param time_points: Список из временных меток.
    :return: None.
    """
    if len(time_points) < 2:
        raise BadTimePoints("Список должен быть как минимум из 2-х временных меток")
    if len(time_points) % 2:
        raise BadTimePoints(
            f"Список должен содержать чётное количество ременных меток. Получили {len(time_points)}"
        )
    for i, time_point in enumerate(time_points[1:]):
        if time_point <= time_points[i]:
            raise BadTimePoints(
                f"Неверные временные точки в списке! "
                f"Временная точка под индексом {i + 1} должна быть больше "
                f"временной точки под индексом {i}."
            )
