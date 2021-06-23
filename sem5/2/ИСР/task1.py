def fibonacci(n):
    fib1, fib2 = 0, 1
    for _ in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


print(list(fibonacci(5)))