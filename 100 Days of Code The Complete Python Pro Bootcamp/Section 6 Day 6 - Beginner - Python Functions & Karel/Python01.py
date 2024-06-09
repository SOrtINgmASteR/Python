# Functions

# Prime Detection
def is_prime(n):
    if (n == 0) or (n == 1):
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Factorial
def factorial(n):
    f = int(1)
    for i in range(1, n + 1):
        f *= i
    return f


# Minimum of 4 numbers
def find_minimum(w, x, y, z):
    minimum = int(w)
    minimum = w if w <= x else x
    minimum = minimum if minimum <= y else y
    minimum = minimum if minimum <= z else z
    return minimum


# Maximum of two numbers
def max_of_two(x, y):
    maximum = x if x >= y else y
    return maximum


# Minimum of two numbers
def min_of_two(x, y):
    minimum = a if x <= y else y
    return minimum


print("Primes between 1 - 100 : ")
for i in range(1, 100 + 1):
    if is_prime(i):
        print(f"{i} is Prime")
    else:
        print(f"{i} is Not Prime")
print()
print("Factorials between 1 - 10 : ")
for i in range(1, 10 + 1):
    fact = int(factorial(i))
    print(f"Factorial of {i} is = {fact}")
print()
a, b, c, d = int(50), int(11), int(23), int(11)
print("Minimum of four numbers : ")
print(find_minimum(a, b, c, d))
