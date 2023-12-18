import re

def perform_calculation(operand1, operator, operand2):
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
    return result

def get_valid_input():
    while True:
        try:
            user_input = input("Enter two real numbers separated by a space: ")
            operand1, operator, operand2 = re.split(r' *([\+\-\*/]) *', user_input)
            operand1, operand2 = float(operand1), float(operand2)
            return operand1, operator, operand2
        except ValueError:
            print("Invalid input. Please enter two valid floating-point numbers.")

def main():
    # Assign values to variables a and b
    a, b = 5, 3

    # Perform basic arithmetic operations
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b:.2f}")

    # Improve program by taking user input
    operand1, operator, operand2 = get_valid_input()

    # Perform user-specified calculation
    result = perform_calculation(operand1, operator, operand2)
    print(f"Result of {operand1} {operator} {operand2} = {result:.2f}")

if __name__ == "__main__":
    main()
