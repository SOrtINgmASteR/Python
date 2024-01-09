# 1074 - Even or Odd
n = int(input())
for i in range(n):
    num = int(input())
    if num == 0:
        print("NULL")
        continue

    if num % 2 == 0:
        print(f"EVEN ", end="")
    elif num % 2 != 0:
        print("ODD ", end="")
    
    if num > 0:
        print("POSITIVE")
    elif num < 0:
        print("NEGATIVE")
