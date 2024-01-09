# 1008 - Salary
employee_ID = int(input())
hours = int(input())
per_Hour = float(input())
salary = hours * per_Hour
print(f"NUMBER = {employee_ID}")
print(f"SALARY = U$ {'{:.2f}'.format(salary)}")
