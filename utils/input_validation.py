from decimal import Decimal, InvalidOperation


def read_decimal(prompt: str) -> Decimal:
    while True:
        try:
            return Decimal(input(prompt).strip())
        except InvalidOperation:
            print("Not a valid number, try again.\n")