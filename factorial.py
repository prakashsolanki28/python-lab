def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

print(factorial(4))

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))


