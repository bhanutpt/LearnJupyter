
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage
n = 10
fib_numbers = fibonacci(n)
print(f"The first {n} Fibonacci numbers are: {fib_numbers}")
