# 1060 - Positive Numbers
count = int(0)
for i in range(0, 6):
    num = float(input())
    if num > 0.00:
        count += 1
print(f"{count} valores positivos")
