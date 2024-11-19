def check_type(func_name, param_name, expected_type, received_value):
    if not isinstance(received_value, expected_type):
        error = TypeError(
            f"In function '{func_name}': Argument '{param_name}' must be of type {expected_type.__name__}, "
            f"but received {type(received_value).__name__}"
        )
        error.__dict__.update(locals())
        raise error


def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        func_name = func.__name__

        # args
        for arg_name, arg_value in zip(annotations.keys(), args):
            expected_type = annotations[arg_name]
            check_type(func_name, arg_name, expected_type, arg_value)

        # kwargs
        for kwarg_name, kwarg_value in kwargs.items():
            if kwarg_name in annotations:
                expected_type = annotations[kwarg_name]
                check_type(func_name, kwarg_name, expected_type, kwarg_value)

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


@strict
def mixed_args(a: int, b: float, c: str, flag: bool) -> str:
    return f"{a}, {b}, {c}, {flag}"


@strict
def only_kwargs(a: int, b: str) -> str:
    return f"{a} and {b}"


@strict
def no_args() -> str:
    return "something"


@strict
def args_and_kwargs(a: int, b: float, c: str, flag: bool = True) -> str:
    return f"{a}, {b}, {c}, {flag}"
