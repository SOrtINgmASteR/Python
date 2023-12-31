# For Loops with range()
for i in range(10, 20, 2):
    print(f"{i} ", end="")
print()

my_numbers = [35, 21, 98, 41, 49, 105, 77, 27, 21, 13, 18]

l = int(len(my_numbers))
for i in range(l):
    print(f"{my_numbers[i]}", end=" ")
print()
for number in my_numbers:
    print(f"{number}", end=" ")
