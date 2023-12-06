# Functions

# Prime Detection
def is_prime(n):
    if (n == 0) or (n == 1):
        return False
    elif n == 2:
        return True
    elif n > 2:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


# Factorial
def factorial(n):
    f = int(1)
    for i in range(1, n+1):
        f *= i
    return f


# Minimum of 4 numbers
def find_minimum(a, b, c, d):
    minimum = int(0)
    minimum = a if a <= b else b
    minimum = minimum if minimum <= c else c
    minimum = minimum if minimum <= d else d
    return minimum


for i in range(1, 100 + 1):
    if is_prime(i):
        print(f"{i} is Prime")
    else:
        print(f"{i} is Not Prime")
print()


for i in range(1, 10+1):
    fact = int(factorial(i))
    print(f"Factorial of {i} is = {fact}")
print()

print(find_minimum(50, 11, 23, 11))
