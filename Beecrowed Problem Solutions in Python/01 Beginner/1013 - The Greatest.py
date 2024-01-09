# 1013 - The Greatest
a, b, c = map(int, input().split())
if a>b:
    if a>c:
        print(f"{a} eh o maior")
    else:
        print(f"{c} eh o maior")
else :
    if b>c:
        print(f"{b} eh o maior")
    else:
        print(f"{c} eh o maior")
