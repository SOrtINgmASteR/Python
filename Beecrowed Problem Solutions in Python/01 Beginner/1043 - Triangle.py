#1043 - Triangle
a, b, c=map(float, input().split(" "))
if a+b>c and b+c>a and a+c>b:
    p=float(a+b+c)
    print(f"Perimetro = {'{:.1f}'.format(p)}")
else :
    a=float(((a+b)/2)*c)
    print(f"Area = {'{:.1f}'.format(a)}")
