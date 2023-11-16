#1045 - Triangle Types
a, b, c = map(float, input().split())
flag=1
if a>=b+c or b>=a+c or c>=a+b:
    print("NAO FORMA TRIANGULO")
    flag=0
elif (a**2)==(b**2)+(c**2) or (b**2)==(a**2)+(c**2) or (c**2)==(a**2)+(b**2):
    print("TRIANGULO RETANGULO")
elif (a**2)>(b**2)+(c**2) or (b**2)>(a**2)+(c**2) or (c**2)>(a**2)+(b**2):
    print("TRIANGULO OBTUSANGULO")
elif ((a**2)<(b**2)+(c**2) or (b**2)<(a**2)+(c**2) or (c**2)<(a**2)+(b**2)):
    print("TRIANGULO ACUTANGULO")

if a==b and b==c and flag==1:
    print("TRIANGULO EQUILATERO")
elif ((a==b and b!=c) or (b==c and b!=a) or (a==c and c!=b)) and flag==1:
    print("TRIANGULO ISOSCELES")
