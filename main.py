# Basic calculator :) 

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def calculate():
    ops = {"+", "-", "*", "/", "**"}
    operation = input(f"Please enter your operation ({', '.join(ops)}): ").strip()

    if operation not in ops:
        print("Invalid operation.")
        return

    prompts = {
        "+": ("Enter your 1st addend: ", "Enter your 2nd addend: "),
        "-": ("Enter your minuend: ", "Enter your subtrahend: "),
        "*": ("Enter your 1st factor: ", "Enter your 2nd factor: "),
        "/": ("Enter your dividend: ", "Enter your divisor: "),
        "**": ("Enter your base number: ", "Enter your power: "),
    }
    p1, p2 = prompts[operation]
    n1 = get_number(p1)
    n2 = get_number(p2)

    if operation == "+":
        result = n1 + n2
    elif operation == "-":
        result = n1 - n2
    elif operation == "*":
        result = n1 * n2
    elif operation == "/":
        if n2 == 0:
            print("Cannot divide by zero.")
            return
        result = n1 / n2
    elif operation == "**":
        result = n1 ** n2

    print(f"{n1} {operation} {n2} = {result}")

def main():
    while True:
        calculate()
        again = input("Calculate again? (y/n): ").strip().lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()
