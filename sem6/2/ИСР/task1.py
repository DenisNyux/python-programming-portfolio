def fibonacci_yield(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1

for fib in fibonacci_yield(20):
    print(fib, end=' ')
print()

def fibonacci_lists(n):
    fibonacci_numbers = [0, 1]
    for i in range(2, n+1):
        fibonacci_numbers.append(fibonacci_numbers[-1]+fibonacci_numbers[-2])
    return fibonacci_numbers

print(fibonacci_lists(20))