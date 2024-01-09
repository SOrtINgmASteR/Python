# 1015 - Distance Between Two Points
import math
x = input().split()
y = input().split()
x1, y1 = x
x2, y2 = y
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)
distance = math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
print(f"{'{:.4f}'.format(distance)}")
