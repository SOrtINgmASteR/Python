# 1094 - Experiments
total = int(0)
C = int(0)
S = int(0)
R = int(0)
t = int(input())
for i in range(t):
    s = input().split(" ")
    animal = str(s[1])
    count = int(s[0])
    total += count
    if animal == "C":
        C += count
    elif animal == "R":
        R += count
    elif animal == "S":
        S += count
coelhos_percentage = float((C / total) * 100)
sapos_percentage = float((S / total) * 100)
ratos_percentage = float((R / total) * 100)

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {C}")
print(f"Total de ratos: {R}")
print(f"Total de sapos: {S}")
print(f"Percentual de coelhos: {'{:.2f}'.format(coelhos_percentage)} %")
print(f"Percentual de ratos: {'{:.2f}'.format(ratos_percentage)} %")
print(f"Percentual de sapos: {'{:.2f}'.format(sapos_percentage)} %")
