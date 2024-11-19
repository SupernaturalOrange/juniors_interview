from solution import (sum_two, concat_strings, divide, logic_and,
                      no_args, only_kwargs, mixed_args, args_and_kwargs)


def check_type_error(exception, func_name, param_name, expected_type, received_value):
    assert exception is not None, f"Expected TypeError for {func_name} and {param_name}"
    assert exception.func_name == func_name, f"Expected func_name: {func_name}, but got: {exception.func_name}"
    assert exception.param_name == param_name, f"Expected param_name: {param_name}, but got: {exception.param_name}"
    assert exception.expected_type == expected_type, \
        f"Expected expected_type: {expected_type}, but got: {exception.expected_type}"
    assert exception.received_value == received_value, \
        f"Expected received_value: {received_value}, but got: {exception.received_value}"


def test_sum_two():
    assert sum_two(1, 2) == 3
    exception = None
    try:
        sum_two(1, 2.0)
    except TypeError as e:
        exception = e
    check_type_error(exception, 'sum_two', 'b', int, 2.0)


def test_concat_strings():
    assert concat_strings("hello", "world") == "helloworld"
    exception = None
    try:
        concat_strings("hello", 123)
    except TypeError as e:
        exception = e
    check_type_error(exception, 'concat_strings', 'b', str, 123)


def test_divide():
    assert divide(4.0, 2.0) == 2.0
    exception = None
    try:
        divide(4.0, "2.0")
    except TypeError as e:
        exception = e
    check_type_error(exception, 'divide', 'b', float, "2.0")


def test_logic_and():
    assert logic_and(True, False) is False
    exception = None
    try:
        logic_and(True, 1)
    except TypeError as e:
        exception = e
    check_type_error(exception, 'logic_and', 'b', bool, 1)


def test_mixed_args():
    assert mixed_args(1, 2.5, "hello", True) == "1, 2.5, hello, True"
    exception = None
    try:
        mixed_args(1, 2.5, 123, True)
    except TypeError as e:
        exception = e
    check_type_error(exception, 'mixed_args', 'c', str, 123)


def test_only_kwargs():
    assert only_kwargs(a=5, b="test") == "5 and test"
    exception = None
    try:
        only_kwargs(a="wrong", b="test")
    except TypeError as e:
        exception = e
    check_type_error(exception, 'only_kwargs', 'a', int, "wrong")


def test_no_args():
    assert no_args() == "something"


def test_args_and_kwargs():
    assert args_and_kwargs(10, 2.5, "test", flag=False) == "10, 2.5, test, False"
    assert args_and_kwargs(1, 3.14, "hello") == "1, 3.14, hello, True"  # flag по умолчанию

    exception = None
    try:
        args_and_kwargs("wrong", 2.5, "test", flag=True)
    except TypeError as e:
        exception = e
    check_type_error(exception, 'args_and_kwargs', 'a', int, "wrong")

    exception = None
    try:
        args_and_kwargs(10, 2.5, "test", flag="not_bool")
    except TypeError as e:
        exception = e
    check_type_error(exception, 'args_and_kwargs', 'flag', bool, "not_bool")


def test():
    test_sum_two()
    test_concat_strings()
    test_divide()
    test_logic_and()
    test_mixed_args()
    test_only_kwargs()
    test_no_args()
    test_args_and_kwargs()
    print("All tests passed!")


if __name__ == "__main__":
    test()
