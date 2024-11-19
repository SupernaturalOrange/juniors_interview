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


def assert_type_error(func, *args, expected_func_name, expected_param_name, expected_type, received_value, **kwargs):
    exception = None
    try:
        func(*args, **kwargs)
    except TypeError as e:
        exception = e
    check_type_error(exception, expected_func_name, expected_param_name, expected_type, received_value)


def test_sum_two():
    assert sum_two(1, 2) == 3
    assert_type_error(
        sum_two, 1, 2.0,
        expected_func_name='sum_two',
        expected_param_name='b',
        expected_type=int,
        received_value=2.0
    )


def test_concat_strings():
    assert concat_strings("hello", "world") == "helloworld"
    assert_type_error(
        concat_strings, "hello", 123,
        expected_func_name='concat_strings',
        expected_param_name='b',
        expected_type=str,
        received_value=123
    )


def test_divide():
    assert divide(4.0, 2.0) == 2.0
    assert_type_error(
        divide, 4.0, "2.0",
        expected_func_name='divide',
        expected_param_name='b',
        expected_type=float,
        received_value="2.0"
    )


def test_logic_and():
    assert logic_and(True, False) is False
    assert_type_error(
        logic_and, True, 1,
        expected_func_name='logic_and',
        expected_param_name='b',
        expected_type=bool,
        received_value=1
    )


def test_mixed_args():
    assert mixed_args(1, 2.5, "hello", True) == "1, 2.5, hello, True"
    assert_type_error(
        mixed_args, 1, 2.5, 123, True,
        expected_func_name='mixed_args',
        expected_param_name='c',
        expected_type=str,
        received_value=123
    )


def test_only_kwargs():
    assert only_kwargs(a=5, b="test") == "5 and test"
    assert_type_error(
        only_kwargs, a="wrong", b="test",
        expected_func_name='only_kwargs',
        expected_param_name='a',
        expected_type=int,
        received_value="wrong"
    )


def test_no_args():
    assert no_args() == "something"


def test_args_and_kwargs():
    assert args_and_kwargs(10, 2.5, "test", flag=False) == "10, 2.5, test, False"
    assert args_and_kwargs(1, 3.14, "hello") == "1, 3.14, hello, True"  # flag по умолчанию

    assert_type_error(
        args_and_kwargs, "wrong", 2.5, "test", flag=True,
        expected_func_name='args_and_kwargs',
        expected_param_name='a',
        expected_type=int,
        received_value="wrong"
    )

    assert_type_error(
        args_and_kwargs, 10, 2.5, "test", flag="not_bool",
        expected_func_name='args_and_kwargs',
        expected_param_name='flag',
        expected_type=bool,
        received_value="not_bool"
    )


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
