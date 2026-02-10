# Calculator Application (Class-Based)

This project is a command-line calculator built in Python using an object-oriented design. The program runs as a REPL (Read–Eval–Print Loop), which allows users to continuously enter arithmetic operations until they choose to exit. The calculator supports addition, subtraction, multiplication, and division, and it safely handles division-by-zero scenarios.

To set up the project, create and activate a virtual environment, then install the required dependencies using `pip install -r requirements.txt`. Once installed, the application can be started with `python main.py`. Commands must follow the format `<operation> <num1> <num2>`, for example `add 2 3`. Typing `exit` will terminate the program.

Unit tests are implemented using **pytest**, and they can be executed with the `pytest` command. Continuous integration is configured with GitHub Actions to ensure all tests pass and that required coverage levels are maintained.

