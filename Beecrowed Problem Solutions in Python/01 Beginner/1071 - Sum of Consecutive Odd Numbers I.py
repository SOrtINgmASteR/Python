# 1071 - Sum of Consecutive Odd Numbers I
a = int(input())
b = int(input())
if a >= b:
    x = int(a)
    y = int(b)
elif a < b:
    x = int(b)
    y = int(a)
sum = int(0)
for i in range(y + 1, x):
    if i % 2 != 0:
        sum += i
print(sum)
