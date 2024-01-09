# 1038 - Snack
s = input().split(" ")
x, y = s;
x = int(x)
y = int(y)
if x == 1:
    ans = float(y * 4)
    print(f"Total: R$ {'{:.2f}'.format(ans)}")
elif x == 2:
    ans = float(y * 4.5)
    print(f"Total: R$ {'{:.2f}'.format(ans)}")
elif x == 3:
    ans = float(y * 5)
    print(f"Total: R$ {'{:.2f}'.format(ans)}")
elif x == 4:
    ans = float(y * 2)
    print(f"Total: R$ {'{:.2f}'.format(ans)}")
elif x == 5:
    ans = float(y * 1.5)
    print(f"Total: R$ {'{:.2f}'.format(ans)}")
