# 1009 - Salary with Bonus
name = str(input())
salary = float(input())
sales = float(input())
total_salary = salary + (sales * 0.15)
print(f"TOTAL = R$ {'{:.2f}'}".format(total_salary))
