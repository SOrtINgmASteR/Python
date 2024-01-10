# 1080 - Highest and Position
max = int(0)
pos = int(0)
for i in range(100):
    number = int(input())
    if number > max:
        max = number
        pos = i + 1
print(f"{max}\n{pos}")
