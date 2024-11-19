def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        for (arg_name, expected_type), arg_value in zip(annotations.items(), args):
            if not isinstance(arg_value, expected_type):
                raise TypeError(f"Argument {arg_name} must be of type {expected_type.__name__}")
        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def concat_strings(a: str, b: str) -> str:
    return a + b


@strict
def divide(a: float, b: float) -> float:
    return a / b


@strict
def logic_and(a: bool, b: bool) -> bool:
    return a and b
