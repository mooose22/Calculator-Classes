import sys
from io import StringIO
from app.calculator import calculator


# Helper function to simulate user input and capture output
def run_calculator_with_input(monkeypatch, inputs):
    input_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_iter))

    captured_output = StringIO()
    sys.stdout = captured_output

    calculator()

    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


# Positive Tests
def test_addition(monkeypatch):
    inputs = ["add 2 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5" in output


def test_subtraction(monkeypatch):
    inputs = ["subtract 5 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 3" in output


def test_multiplication(monkeypatch):
    inputs = ["multiply 4 5", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 20" in output


def test_division(monkeypatch):
    inputs = ["divide 10 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5.0" in output


# Negative Tests
def test_invalid_operation(monkeypatch):
    inputs = ["modulus 5 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Unknown operation." in output


def test_invalid_number_input(monkeypatch):
    inputs = ["add two three", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Numbers must be valid." in output


def test_invalid_input_format(monkeypatch):
    inputs = ["add 5", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Format: <operation> <num1> <num2>" in output


def test_division_by_zero(monkeypatch):
    inputs = ["divide 5 0", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error: cannot divide by zero" in output
