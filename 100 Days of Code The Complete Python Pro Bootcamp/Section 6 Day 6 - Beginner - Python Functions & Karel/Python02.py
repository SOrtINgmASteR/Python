# While Loops

# Digit Sum
def digit_summation(n):
    digit_sum = int(0)
    last_digit = int(0)
    while n != 0:
        last_digit = n % 10
        digit_sum += last_digit
        n //= 10
    return digit_sum


# Digit Count
def digit_count(n):
    count = int(0)
    while n != 0:
        n //= 10
        count += 1
    return count


# Number Reverse
def number_reverse(n):
    reverse_number = int(0)
    last_digit = int(0)
    while n != 0:
        last_digit = n % 10;
        reverse_number *= 10
        reverse_number += last_digit
        n //= 10
    return reverse_number


print(digit_summation(123))
print(number_reverse(3456))
print(digit_count(5470))
