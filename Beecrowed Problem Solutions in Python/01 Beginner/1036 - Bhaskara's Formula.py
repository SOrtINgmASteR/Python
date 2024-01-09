# 1036 - Bhaskara's Formula
import math
s = input().split(" ")
a, b, c = s
a = float(a)
b = float(b)
c = float(c)

root = float((b ** 2) - 4 * a * c)
if root >= 0 and a != 0:
    solve_1 = float((- b + math.sqrt(root)) / (2 * a))
    solve_2 = float((- b - math.sqrt(root)) / (2 * a))
    print(f"R1 = {'{:.5f}'.format(solve_1)}")
    print(f"R2 = {'{:.5f}'.format(solve_2)}")
else:
    print("Impossivel calcular")
