# 1048 -  Salary Increase
salary = float(input())
if salary >= 0 and salary <= 400.00:
    bouns = float(salary * 0.15)
    new_salary = float(salary + bouns)
    print(f"Novo salario: {'{:.2f}'.format(new_salary)}")
    print(f"Reajuste ganho: {'{:.2f}'.format(bouns)}")
    print("Em percentual: 15 %")
elif salary > 400.00 and salary <= 800.00:
    bouns = float(salary * 0.12)
    new_salary = float(salary + bouns)
    print(f"Novo salario: {'{:.2f}'.format(new_salary)}")
    print(f"Reajuste ganho: {'{:.2f}'.format(bouns)}")
    print("Em percentual: 12 %")
elif salary > 800.00 and salary <= 1200.00:
    bouns = float(salary * 0.10)
    new_salary = float(salary + bouns)
    print(f"Novo salario: {'{:.2f}'.format(new_salary)}")
    print(f"Reajuste ganho: {'{:.2f}'.format(bouns)}")
    print("Em percentual: 10 %")
elif salary > 1200.00 and salary <= 2000.00:
    bouns = float(salary * 0.07)
    new_salary = float(salary + bouns)
    print(f"Novo salario: {'{:.2f}'.format(new_salary)}")
    print(f"Reajuste ganho: {'{:.2f}'.format(bouns)}")
    print("Em percentual: 7 %")
elif salary > 2000.00:
    bouns = float(salary * 0.04)
    new_salary = float(salary + bouns)
    print(f"Novo salario: {'{:.2f}'.format(new_salary)}")
    print(f"Reajuste ganho: {'{:.2f}'.format(bouns)}")
    print("Em percentual: 4 %")
