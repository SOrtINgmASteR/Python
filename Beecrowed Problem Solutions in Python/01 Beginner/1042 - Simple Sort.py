# 1042 - Simple Sort
numbers=[]
s = input().split(" ")
a, b, c = s
a = int(a)
b = int(b)
c = int(c)
numbers.append(a)
numbers.append(b)
numbers.append(c)
numbers.sort()
print(numbers[0])
print(numbers[1])
print(numbers[2])
print()
print(a)
print(b)
print(c)
