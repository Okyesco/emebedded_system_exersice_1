def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n + 1):
        fib_series.append(fib_series[i - 1] + fib_series[i - 2])
    return fib_series

def get_max_limit():
    while True:
        try:
            max_limit = int(input("Enter the maximum number up to which to calculate Fibonacci numbers: "))
            if max_limit < 0:
                raise ValueError("Please enter a non-negative integer.")
            return max_limit
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

def main():
    max_limit = get_max_limit()
    fib_series = fibonacci(max_limit)

    print(f"Fibonacci numbers up to F({max_limit}): {fib_series}")

if __name__ == "__main__":
    main()
