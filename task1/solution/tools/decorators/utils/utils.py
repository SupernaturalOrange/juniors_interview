import inspect
from typing import Any, Callable


def type_validation(
    func: Callable[[Any], Any], *args: Any, **kwargs: Any
) -> tuple[bool, str]:
    """
    Функция соответствия типов передаваемых аргументов.

    :param func: Анализируемая функция.
    :param args: Позиционные аргументы.
    :param kwargs: Именованные аргументы.
    :return: Если типы передаваемых аргументов не соответствуют типам аргументов,
        объявленных в прототипе функции, то будет возвращено (False, message), иначе (True, message),
        где message - это сообщение об ошибке, если возвращается False, иначе пустой str.
    """
    sig = inspect.signature(func)

    bound_arguments = sig.bind(*args, **kwargs)
    for name, value in bound_arguments.arguments.items():
        expected_type = sig.parameters[name].annotation
        if expected_type is not inspect.Parameter.empty and not isinstance(
            value, expected_type
        ):
            return (
                False,
                f"Аргумент '{name}' должен быть типа {expected_type}, получен {type(value)}.",
            )

    return True, ""
