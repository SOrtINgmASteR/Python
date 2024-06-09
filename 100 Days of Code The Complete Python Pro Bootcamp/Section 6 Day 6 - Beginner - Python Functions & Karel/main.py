def max_of_two(a, b):
    maximum = a if a >= b else b
    return maximum


def min_of_two(a, b):
    minimum = a if a <= b else b
    return minimum


def is_prime(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    for i in range(1, 100 + 1):
        if is_prime(i):
            print(f"{i} is Prime.")
        else:
            print(f"{i} is not Prime.")


main()
