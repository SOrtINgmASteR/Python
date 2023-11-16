#1019 - Time Conversion
S=int(input())
h=int(S//3600)
S-=(3600*h)
m=int(S//60)
S-=(60*m)
s=int(S)
print(f"{h}:{m}:{s}")
