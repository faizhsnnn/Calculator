from ascii import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero."
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply, 
    "/" : divide,
}

def calculator():
    print(logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")

        if operation_symbol not in operations:
            print("Invalid operation! Try again.\n")
            continue

        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue with {answer}, or 'n' to start a new calculation, or 'q' to quit: ").lower()

        if choice == "y":
            num1 = answer
        elif choice == "n":
            print("\n" * 50)
            calculator()  
            return
        else:
            print("Goodbye!")
            return

calculator()
