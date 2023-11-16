#1012 - Area
string = input().split(" ")
a, b, c = string
a=float(a)
b=float(b)
c=float(c)
triangle=0.5*a*c
circle= 3.14159*(c**2)
trapezium=((a+b)/2)*c
square=b**2
rectangle=a*b
print(f"TRIANGULO: {'{:.3f}'.format(triangle)}")
print(f"CIRCULO: {'{:.3f}'.format(circle)}")
print(f"TRAPEZIO: {'{:.3f}'.format(trapezium)}")
print(f"QUADRADO: {'{:.3f}'.format(square)}")
print(f"RETANGULO: {'{:.3f}'.format(rectangle)}")
