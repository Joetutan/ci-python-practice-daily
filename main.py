from app.calculator import Calculator
from utils.input_validation import read_decimal


def main():

    while True:
        cmd = (
            input("Choose action (add,subtract,multiply,divide,exit)...\n")
            .strip()
            .lower()
        )
        try:
            match cmd:
                case "add":
                    print("Add two numbers \n")
                    num1 = read_decimal("Enter first number...\n")
                    num2 = read_decimal("Enter second number...\n")
                    total = Calculator.add(num1, num2)
                    print(f"{num1} + {num2} = {total}")
                case "exit":
                    break
                case _:
                    print("Invalid input try again...\n")

        except ZeroDivisionError as exc:
            print(f"Error: {exc}\n")


if __name__ == "__main__":
    main()
