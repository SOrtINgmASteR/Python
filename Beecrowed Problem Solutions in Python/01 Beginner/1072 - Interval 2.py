#1072 - Interval 2
in_range=int(0)
out_range=int(0)
t=int(input())
for i in range(0, t):
    n=int(input())
    if(n>=10 and n<=20):
        in_range+=1
    else:
        out_range+=1
print(f"{in_range} in")
print(f"{out_range} out")
