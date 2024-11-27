from typing import Optional, Tuple


class PeriodTime:
    """
    Класс отрезков времени.
    """

    def __init__(self, time_period: Tuple[int, int]):
        self.validate_period(time_period[0], time_period[1])
        self.__time_in = time_period[0]
        self.__time_out = time_period[1]

    @property
    def time_in(self) -> int:
        """
        Вернёт начало отрезка времени.

        :return: Начало отрезка времени (int).
        """
        return self.__time_in

    @time_in.setter
    def time_in(self, time_in: int) -> None:
        """
        Задаёт начало отрезка времени.

        :param time_in: Начало отрезка времени (int).
        :return: None.
        """
        self.validate_period(time_in, self.time_out)
        self.__time_in = time_in

    @property
    def time_out(self) -> int:
        """
        Вернёт конец отрезка времени.

        :return: Конец отрезка времени (int).
        """
        return self.__time_out

    @time_out.setter
    def time_out(self, time_out: int) -> None:
        """
        Задаёт конец отрезка времени.

        :param time_out: Конец отрезка времени (int).
        :return: None.
        """
        self.validate_period(self.time_in, time_out)
        self.__time_out = time_out

    @staticmethod
    def validate_period(time_in: int, time_out: int) -> None:
        """
        Функция проверит, что начало отрезка времени меньше конечного,
        иначе вызовет исключение ValueError.

        :param time_in: Начало отрезка времени (int).
        :param time_out: Конец отрезка времени (int)
        :return: None.
        """
        if time_out < time_in:
            raise ValueError("Начало отрезка времени должно быть меньше конечного.")

    def __repr__(self) -> str:
        """
        Возвращает строковое представление экземпляра для отладки.
        :return: Строковое представление экземпляра (str).
        """
        return f"PeriodTime({self.time_in}, {self.time_out})"

    def intersection(self, period: "PeriodTime") -> Optional["PeriodTime"]:
        """
        Вернёт общий временной отрезок PeriodTime, если такой существует, иначе None.

        :param period: Другой временной отрезок (PeriodTime).
        :return: Общий временной отрезок PeriodTime, если такой существует, иначе None.
        """
        if not period.time_out > self.time_in or not period.time_in < self.time_out:
            return None
        intersection_time_in = max(self.time_in, period.time_in)
        intersection_time_out = min(self.time_out, period.time_out)
        return PeriodTime((intersection_time_in, intersection_time_out))

    def get_time(self) -> int:
        """
        Вернёт время отрезка в секундах.

        :return: Время отрезка (int).
        """

        return self.time_out - self.time_in

    def __eq__(self, other: object) -> bool:
        """
        Функция сравнения.
        :param other: Другой временной отрезок (PeriodTime).
        :return: True, если time_in и time_out у обоих равны, иначе False.
        """
        if not isinstance(other, PeriodTime):
            return False
        return self.time_in == other.time_in and self.time_out == other.time_out


class BadTimePoints(Exception):
    pass
