def get_user_angle():
    while True:
        try:
            angle_degrees = float(input("Enter an angle in degrees: "))
            return angle_degrees
        except ValueError:
            print("Invalid input. Please enter a numeric value for the angle.")

def calculate_sine(angle_degrees):
    # Convert degrees to radians using the approximation: radians = degrees * (pi / 180)
    pi = 3.141592653589793
    angle_radians = angle_degrees * (pi / 180)

    # Taylor series expansion for sine function
    sine_value = angle_radians
    sign = -1
    for i in range(3, 22, 2):  # Iterate through odd terms up to 19 (inclusive)
        term = (angle_radians ** i) / factorial(i)
        sine_value += sign * term
        sign *= -1

    return sine_value

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    angle_degrees = get_user_angle()
    sine_value = calculate_sine(angle_degrees)

    print(f"The sine of {angle_degrees} degrees is: {sine_value:.4f}")

if __name__ == "__main__":
    main()
