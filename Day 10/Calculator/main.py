from replit import clear
from art import logo

operation = {
    "Addition": "+",
    "Subtraction": "-",
    "Multiplication": "*",
    "Division": "/",
}


def continuation(answer):
    while True:
        global operation
        print(logo)
        print(f"Current number: {answer}")
        print("-----------------")
        for key, value in operation.items():
            print(f"{key}: {value}")
        print("-----------------")
        ops = input("Pick an operation: ")
        next = float(input("What's the next number: "))
        new = calculator(answer, next, ops)
        print(f"{answer} {ops} {next} = {new}")
        ask = input(
            f"Type 'y' to continue calculating with {new} or type 'n' to start new calculation: "
        ).lower()
        while ask not in ("y", "n"):
            ask = input(
                f"Type 'y' to continue calculating with {new} or type 'n' to start new calculation: "
            ).lower()

        if ask == "y":
            answer = new
            clear()
            continue
        elif ask == "n":
            clear()
            calc()


def calculator(num1, num2, operations):
    if operations == "+":
        return num1 + num2
    elif operations == "-":
        return num1 - num2
    elif operations == "*":
        return num1 * num2
    elif operations == "/":
        return num1 / num2


def calc():
    while True:
        print(logo)
        num1 = float(input("What's the first number? "))
        print("-----------------")
        for key, value in operation.items():
            print(f"{key}: {value}")
        print("-----------------")
        operations = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        answer = calculator(num1, num2, operations)
        print(f"{num1} {operations} {num2} = {answer}")

        ask = input(
            f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation: "
        ).lower()
        while ask not in ("y", "n", "end"):
            ask = input(
                f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation:   "
            ).lower()

        if ask == "y":
            clear()
            continuation(answer)
        elif ask == "n":
            clear()
            continue


calc()
