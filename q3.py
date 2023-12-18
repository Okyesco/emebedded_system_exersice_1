def get_valid_integer_input():
    while True:
        try:
            user_input = input("Please enter two integer numbers separated by a space: ")
            values = user_input.split()
            if len(values) != 2:
                raise ValueError("Please enter exactly 2 integer values.")
            value1, value2 = map(int, values)
            return value1, value2
        except ValueError as e:
            print(f"Error: {e}. Please enter two correct integer numbers.")

def main():
    a, b = 5, 7

    # Check which number is bigger
    if a > b:
        print(f"The first value ({a}) is bigger than the second value ({b}).")
    elif a < b:
        print(f"The second value ({b}) is bigger than the first value ({a}).")
    else:
        print("Both values are equal.")

    # Improve program by taking user input for integer numbers
    value1, value2 = get_valid_integer_input()

    # Compare user-inputted integer values
    if value1 > value2:
        print(f"The first value ({value1}) is bigger than the second value ({value2}).")
    elif value1 < value2:
        print(f"The second value ({value2}) is bigger than the first value ({value1}).")
    else:
        print("Both values are equal.")

if __name__ == "__main__":
    main()
