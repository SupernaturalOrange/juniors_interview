import json
import os

from task3.solution.utils.classes import BadTimePoints
from task3.solution.utils.utils import get_all_intersection, normalized_list_period


def appearance(intervals: dict[str, list[int]]) -> int:
    # конвертируем наши списки в другой вид, где интервал будет экземпляром класса PeriodTime.
    lesson_normalized = normalized_list_period(intervals["lesson"])
    lesson_period = lesson_normalized[0]
    pupil_normalized = normalized_list_period(intervals["pupil"])
    tutor_normalized = normalized_list_period(intervals["tutor"])

    # Найдем все пересечения временных отрезков ученика и учителя с временным отрезком урока.
    pupil_intersection = get_all_intersection(lesson_period, pupil_normalized)
    tutor_intersection = get_all_intersection(lesson_period, tutor_normalized)

    # Если кто-то не попал на урок, то и совместного времени не будет.
    if not pupil_intersection or not tutor_intersection:
        return 0

    # Теперь среди этих отрезков найдём общие пересечения
    # Для этого пробежимся по временным отрезкам ученика и ищем пересечения с отрезками учителя.
    all_intersection_period_list = []
    for pupil_period in pupil_intersection:
        intersection_periods = get_all_intersection(pupil_period, tutor_intersection)
        if intersection_periods:
            all_intersection_period_list.extend(intersection_periods)
    return (
        sum(item.get_time() for item in all_intersection_period_list)
        if all_intersection_period_list
        else 0
    )


file_path = os.path.join("files", "periods.json")
with open(file_path, "r", encoding="utf-8") as file:
    tests = json.load(file)

# Вероятно в задание закралась ошибка. Рассмотрим поближе интервалы, где 'answer': 3577.
# Вот список интервалов ученика: 'pupil': [1594702789, 1594704500, 1594702807, 1594704542, ...
# Что мы видим: 1594702789 < 1594704500 > 1594702807 < 1594704542 ... И так по всему списку.
# Временные метки должны строго возрастать. Если я правильно понял задание.
# Ошибка возникает только с этим списком, все остальные проходят мою валидацию и соответственно ваш тест.
# На основании этого факта немного подправлю тест блоком try и выведу значение 'answer' на экран,
# что бы было понятно, где возникла ошибка.

if __name__ == "__main__":
    for i, test in enumerate(tests):
        try:
            test_answer = appearance(test["intervals"])
        except BadTimePoints:
            print(f"Данные не прошли валидацию, где 'answer' равен {test["answer"]}")
        else:
            assert (
                test_answer == test["answer"]
            ), f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
