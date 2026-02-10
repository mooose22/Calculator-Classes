import pytest
from app.operations import CalculatorOperations


ops = CalculatorOperations()


def test_add_positive():
    assert ops.add(2, 3) == 5
    assert ops.add(0, 0) == 0
    assert ops.add(-1, 1) == 0


def test_add_negative():
    assert ops.add(-2, -3) == -5
    assert ops.add(-1, 0) == -1


def test_subtract_positive():
    assert ops.subtract(5, 3) == 2
    assert ops.subtract(10, 5) == 5
    assert ops.subtract(0, 0) == 0


def test_subtract_negative():
    assert ops.subtract(-5, -3) == -2
    assert ops.subtract(3, 5) == -2


def test_multiply_positive():
    assert ops.multiply(2, 3) == 6
    assert ops.multiply(0, 10) == 0
    assert ops.multiply(-2, -3) == 6


def test_multiply_negative():
    assert ops.multiply(2, -3) == -6
    assert ops.multiply(-2, 3) == -6


def test_divide_positive():
    assert ops.divide(6, 3) == 2
    assert ops.divide(-6, -3) == 2


def test_divide_negative():
    assert ops.divide(6, -3) == -2
    assert ops.divide(-6, 3) == -2


def test_divide_by_zero():
    assert ops.divide(1, 0) == "Error: cannot divide by zero"

