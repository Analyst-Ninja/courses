import time

import pytest
import src.my_functions as my_functions


def test_add():
    result = my_functions.add(a=5, b=10)
    assert result == 15


def test_add_string():
    result = my_functions.add(a="I like ", b="burgers")
    assert result == "I like burgers"


def test_divide():
    result = my_functions.divide(a=10, b=10)
    assert result == 1


@pytest.mark.slow("It takes a sleep time")
def test_very_slow():
    time.sleep(1)
    result = my_functions.divide(a=10, b=10)
    assert result == 1


@pytest.mark.skip(reason="This feature is currently broken")
def test_add_skip():
    assert my_functions.add(a=5, b=2) == 7


@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_by_zero():
    assert my_functions.divide(a=3, b=2)
