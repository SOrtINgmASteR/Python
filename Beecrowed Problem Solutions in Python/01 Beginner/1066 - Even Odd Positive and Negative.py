#1066 - Even, Odd, Positive and Negative
even=int(0)
odd=int(0)
positive=int(0)
negative=int(0)
for i in range(0, 5):
    num=int(input())
    if num%2==0:
        even+=1
    elif num%2!=0:
        odd+=1
    
    if num>0:
        positive+=1
    elif num<0:
        negative+=1

print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{positive} valor(es) positivo(s)")
print(f"{negative} valor(es) negativo(s)")
