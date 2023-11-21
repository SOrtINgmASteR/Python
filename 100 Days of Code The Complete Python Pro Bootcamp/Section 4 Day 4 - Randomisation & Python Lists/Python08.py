# List organizing methods
my_numbers = [5, -3, 2, 14, 1, 34, -24, -3, -8]

# Not permanent sort
print(f"Not permanent Sorting : {sorted(my_numbers)}")
print(f"Original List : {my_numbers}")
print(f"Not permanent Sorting : {sorted(my_numbers, reverse=True)}")
print(f"Original List : {my_numbers}")

# Permanent sort
my_numbers.sort()
print(my_numbers)
my_numbers.sort(reverse=True)
print(my_numbers)