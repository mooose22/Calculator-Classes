import pytest
from app.operations import add, subtract, multiply, divide


def test_add_positive():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0


def test_add_negative():
    assert add(-2, -3) == -5
    assert add(-1, 0) == -1


def test_subtract_positive():
    assert subtract(5, 3) == 2
    assert subtract(10, 5) == 5
    assert subtract(0, 0) == 0


def test_subtract_negative():
    assert subtract(-5, -3) == -2
    assert subtract(3, 5) == -2


def test_multiply_positive():
    assert multiply(2, 3) == 6
    assert multiply(0, 10) == 0
    assert multiply(-2, -3) == 6


def test_multiply_negative():
    assert multiply(2, -3) == -6
    assert multiply(-2, 3) == -6


def test_divide_positive():
    assert divide(6, 3) == 2
    assert divide(-6, -3) == 2


def test_divide_negative():
    assert divide(6, -3) == -2
    assert divide(-6, 3) == -2


def test_divide_by_zero():
    assert divide(1, 0) == "Error: cannot divide by zero"
