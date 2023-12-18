class MathSeriesCalculator:
    @staticmethod
    def fibonacci_up_to_n(n):
        fib_series = [0, 1]
        while fib_series[-1] + fib_series[-2] <= n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

    @staticmethod
    def fibonacci_smaller_than_max(max_value):
        fib_series = [0, 1]
        while fib_series[-1] + fib_series[-2] < max_value:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

    @staticmethod
    def primes_up_to_max(max_value):
        primes = []
        for num in range(2, max_value + 1):
            is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
            if is_prime:
                primes.append(num)
        return primes

    @staticmethod
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    @staticmethod
    def geometric_series(a, r, n):
        return [a * r**i for i in range(n)]

    @staticmethod
    def harmonic_series(n):
        return [1 / i for i in range(1, n + 1)]

# Example usage:
calculator = MathSeriesCalculator()

# 1. Fibonacci numbers up to F(n)
fibonacci_n = calculator.fibonacci_up_to_n(20)
print("Fibonacci up to F(20):", fibonacci_n)

# 2. Fibonacci numbers smaller than max
fibonacci_max = calculator.fibonacci_smaller_than_max(100)
print("Fibonacci smaller than 100:", fibonacci_max)

# 3. Prime numbers up to max
primes_max = calculator.primes_up_to_max(30)
print("Primes up to 30:", primes_max)

# 4. Factorial
factorial_result = calculator.factorial(5)
print("Factorial of 5:", factorial_result)

# 5. Geometric series
geometric_series_result = calculator.geometric_series(2, 3, 5)
print("Geometric series (a=2, r=3, n=5):", geometric_series_result)

# 6. Harmonic series
harmonic_series_result = calculator.harmonic_series(5)
print("Harmonic series (n=5):", harmonic_series_result)
