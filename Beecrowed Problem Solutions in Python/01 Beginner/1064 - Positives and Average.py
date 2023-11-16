#1064 - Positives and Average
count=int(0)
avg=float(0.00)
sum=float(0.00)
for i in range(0, 6):
    num=float(input())
    if(num>0.00):
        count+=1
        sum+=num
if count>=1:
    avg=float(sum/count)
print(f"{count} valores positivos")
print(f"{'{:.1f}'.format(avg)}")
