# Exercise - Lesson  21 - Prime Numbers
def prime_checker(number):
    if number == 0 or number == 1:
        print("It's not a prime number.")
        return
    elif number == 2:
        print("It's a prime number.")
        return
    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number.")
            return
    print("It's a prime number.")
    return


n = int(input("Enter Number : "))
prime_checker(number=n)
