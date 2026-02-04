from app.operations import add, subtract, multiply, divide

def calculator():
    print("Simple Calculator")
    print("Format: <operation> <num1> <num2>")
    print("Operations: add, subtract, multiply, divide")
    print("Example: add 2 3")
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
            result = add(a, b)
        elif op == "subtract":
            result = subtract(a, b)
        elif op == "multiply":
            result = multiply(a, b)
        elif op == "divide":
            result = divide(a, b)
        else:
            print("Unknown operation.")
            continue

        print("Result:", result)
