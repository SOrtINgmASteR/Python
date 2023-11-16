#1065 - Even Between five Numbers
count=int(0)
for i in range(0, 5):
    num=int(input())
    if(num%2==0):
        count+=1
print(f"{count} valores pares")
