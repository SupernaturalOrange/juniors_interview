from solution import sum_two, concat_strings, divide, logic_and


def test_sum_two():
    assert sum_two(1, 2) == 3
    try:
        sum_two(1, 2.0)
    except TypeError as e:
        assert str(e) == "Argument b must be of type int"
    else:
        assert False


def test_concat_strings():
    assert concat_strings("hello", "world") == "helloworld"
    try:
        concat_strings("hello", 123)
    except TypeError as e:
        assert str(e) == "Argument b must be of type str"
    else:
        assert False


def test_divide():
    assert divide(4.0, 2.0) == 2.0
    try:
        divide(4.0, "2.0")
    except TypeError as e:
        assert str(e) == "Argument b must be of type float"
    else:
        assert False


def test_logic_and():
    assert logic_and(True, False) is False
    try:
        logic_and(True, 1)
    except TypeError as e:
        assert str(e) == "Argument b must be of type bool"
    else:
        assert False


def test():
    test_sum_two()
    test_concat_strings()
    test_divide()
    test_logic_and()
    print("All tests passed!")


if __name__ == "__main__":
    test()
