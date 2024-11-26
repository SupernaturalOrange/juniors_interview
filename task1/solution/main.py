from task1.solution.tools.decorators.decorators import strict


@strict
def sum_two(a: int, b: int) -> int:
    """
    Функция сложения двух целых чисел.

    :param a: Первое целое число для сложения (int).
    :param b: Второе целое число для сложения (int).
    :return: Сумма двух целых чисел (int).
    """
    return a + b


# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
