from app.operations import CalculatorOperations

def calculator():
    ops = CalculatorOperations()

    print("Simple Calculator")
    print("Format: <operation> <num1> <num2>")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("> ").strip().lower()

        if user_input == "exit":
            print("Goodbye!")
            break

        parts = user_input.split()
        if len(parts) != 3:
            print("Format: <operation> <num1> <num2>")
            continue

        op, a, b = parts

        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print("Numbers must be valid.")
            continue

        if op == "add":
            result = ops.add(a, b)
        elif op == "subtract":
            result = ops.subtract(a, b)
        elif op == "multiply":
            result = ops.multiply(a, b)
        elif op == "divide":
            result = ops.divide(a, b)
        else:
            print("Unknown operation.")
            continue

        print("Result:", result)
