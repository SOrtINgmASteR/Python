# List insertion & deletion methods
my_numbers = [5, -3, 2, 14, 1, 34, -24, -3, -8]

# insertion methods
my_numbers.insert(2, 68)
my_numbers.insert(3, 70)
print(my_numbers)

my_numbers.append(54)
my_numbers.append(34)
print(my_numbers)

my_numbers.extend([84, -62, -34, 44, 66, 68, 11])
print(my_numbers)

# deletion methods
my_numbers.remove(68)
my_numbers.remove(11)
print(my_numbers)

pop_value = my_numbers.pop(5)
print(f"pop value {pop_value}")
pop_value = my_numbers.pop()
print(f"pop value {pop_value}")
print(my_numbers)

del my_numbers[5]
del my_numbers[1]
print(my_numbers)