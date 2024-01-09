# 1020 - Age in Days
D = int(input())
y = int(D // 365)
D -= (y * 365)
m = int(D // 30)
D -= (m*30)
d = D
print(f"{y} ano(s)")
print(f"{m} mes(es)")
print(f"{d} dia(s)")
