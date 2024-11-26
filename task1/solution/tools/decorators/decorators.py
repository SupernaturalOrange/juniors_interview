from functools import wraps
from typing import Callable, ParamSpec, TypeVar

from task1.solution.tools.decorators.utils.utils import type_validation

T = TypeVar("T")
P = ParamSpec("P")


def strict(func: Callable[P, T]) -> Callable[P, T]:
    """
    Декоратор соответствия типов передаваемых аргументов.
    Если типы передаваемых аргументов не соответствуют типам аргументов,
    объявленных в прототипе функции, то будет вызвано исключение TypeError.
    """

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        result, message = type_validation(func, *args, **kwargs)
        if not result:
            raise TypeError(message)
        return func(*args, **kwargs)

    return wrapper
