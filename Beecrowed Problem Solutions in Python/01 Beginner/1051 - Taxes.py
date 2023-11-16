#1051 - Taxes
salary=float(input())
if salary<=2000.00:
    print("Isento")
elif salary>2000.00 and salary<=3000.00:
    tax=float((salary-2000.00)*0.08)
    print(f"R$ {'{:.2f}'.format(tax)}")
elif salary>3000.00 and salary<=4500.00:
    tax=float((1000.00*0.08)+(salary-3000.00)*0.18)
    print(f"R$ {'{:.2f}'.format(tax)}")
elif salary>4500.00:
    tax=float((1000.00*0.08)+(1500.00*0.18)+(salary-4500.00)*0.28)
    print(f"R$ {'{:.2f}'.format(tax)}")
