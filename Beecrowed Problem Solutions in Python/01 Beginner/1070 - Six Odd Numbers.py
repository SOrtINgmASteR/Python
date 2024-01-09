# 1070 - Six Odd Numbers
count = int(6)
n = int(input())
while count != 0:
    if(n % 2 != 0):
        print(n)
        count -= 1
    n += 1
