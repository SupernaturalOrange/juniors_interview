# type: ignore
"""Test timestamp"""

def appearance(intervals: dict[str, list[int]]) -> int:
    """Возвращает время общего присутствия ученика и учителя на уроке."""
    lesson = intervals['lesson']
    tutor = intervals['tutor']
    pupil = intervals['pupil']
    len_pupil = len(pupil)
    len_tutor = len(tutor)
    lesson_timepoints = set(range(lesson[-2], lesson[-1]))

    def _timepoints_person(
            time_points_: list, range_iter: int, cur_lesson: list
    ) -> set:
        """Создаем временные точки на отрезках времени."""
        time_points = set()
        for part_index in range(0, range_iter - 2, 2):
            time_points = (
                    time_points |
                    set(
                        range(
                            time_points_[part_index],
                            time_points_[part_index + 1]
                        )
                    )
            )
        else:
            time_points = (
                    time_points |
                    set(range(time_points_[-2], time_points_[-1]))
            )

        return time_points

    time_points_stud = _timepoints_person(
        time_points_=pupil, range_iter=len_pupil, cur_lesson=lesson
    )
    time_points_teacher = _timepoints_person(
        time_points_=tutor, range_iter=len_tutor, cur_lesson=lesson
    )

    return len(time_points_stud & time_points_teacher & lesson_timepoints)


tests: list[dict[str, int | dict[str, list[int]]]] = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        try:
            assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
        except AssertionError:
            print(f'Error on test case {i}, got {test_answer}')
