"""Test decorator strict"""

import inspect
import logging
from functools import wraps
from string import Template
from typing import Callable

logger = logging.getLogger(__name__)


def strict(func: Callable) -> Callable:
    """Декоратор проверяет соответствие типов."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper."""
        annotations = inspect.signature(func).parameters
        error_msg = Template(
            "Требуемый тип $arg_type, было передано $arg_type2, тип: $type"
        )
        return_annotation = inspect.signature(func).return_annotation

        try:
            for index, type_arg in enumerate(annotations.values()):
                if val := kwargs.get(type_arg.name):
                    if not isinstance(val, type_arg.annotation):
                        raise TypeError(
                            error_msg.substitute(
                                arg_type=type_arg.annotation.__name__,
                                arg_type2=str(val),
                                type=type(val).__name__,
                            )
                        )
                else:
                    if not isinstance(args[index], type_arg.annotation):
                        raise TypeError(
                            error_msg.substitute(
                                arg_type=type_arg.annotation.__name__,
                                arg_type2=args[index],
                                type=type(args[index]).__name__,
                            )
                        )

            result = func(*args, **kwargs)

            if return_annotation and not isinstance(result, return_annotation):
                raise TypeError(
                    error_msg.substitute(
                        arg_type=return_annotation.__name__,
                        arg_type2=args[result],
                        type=type(result).__name__,
                    )
                )

        except TypeError as er:
            logger.error(er)
            raise TypeError(er)

    return wrapper


@strict
def my_func(params: dict, value: int, comment: str) -> bool:
    logger.info(f"params: {params}, value: {value}, comment: {comment}")
    return True


try:
    my_func(params={"a": 1, "b": 2, "c": 3}, value=ValueError, comment="test")
except TypeError as error:
    logger.error(error)

my_func(params={"a": 1, "b": 2, "c": 3}, value=22, comment="test")

my_func({"a": 1, "b": 2, "c": 3}, 22, "test")

try:
    my_func({"a": 1, "b": 2, "c": 3}, 22.22, comment="ValueError")
except TypeError as error:
    logger.error(error)

try:
    my_func({"a": 1, "b": 2, "c": 3}, value=22.22, comment="ValueError")
except TypeError as error:
    logger.error(error)


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
try:
    print(sum_two(1, 2.4))  # >>> TypeError
except TypeError as error:
    logger.error(error)
