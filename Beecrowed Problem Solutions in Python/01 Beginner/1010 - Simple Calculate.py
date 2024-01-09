# 1010 - Simple Calculate
x = input().split(" ")
y = input().split(" ")
id_1, unit_1, per_unit_1 = x
id_2, unit_2, per_unit_2 = y
total = int(unit_1) * float(per_unit_1) + int(unit_2) * float(per_unit_2)
print(f"VALOR A PAGAR: R$ {'{:.2f}'.format(total)}")
