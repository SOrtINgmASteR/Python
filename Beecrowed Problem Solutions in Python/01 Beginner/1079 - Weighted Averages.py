# 1079 - Weighted Averages
t = int(input())
for i in range(t):
    a, b, c = map(float, input().split(" "))
    average = ((a * 2) + (b * 3) + (c * 5)) / (2 + 3 + 5)
    print(f"{'{:.1f}'.format(average)}")
