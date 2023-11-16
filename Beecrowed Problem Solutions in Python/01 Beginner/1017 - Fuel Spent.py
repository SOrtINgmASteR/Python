#1017 - Fuel Spent
time=int(input())
speed=int(input())
distance=time*speed
fuel=distance*(1/12)
print(f"{'{:.3f}'.format(fuel)}")
