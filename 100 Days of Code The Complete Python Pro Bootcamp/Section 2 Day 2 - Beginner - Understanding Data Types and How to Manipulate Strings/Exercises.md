<h2 style="text-align:center">DAY - 2</h2>  

<h3 style="text-align:center;">Lesson 5 - Data Types</h3>  

```python
two_digit_number = str(input())
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
sum_of_digits = first_digit + second_digit
print(f"{sum_of_digits}")
```  

<h3 style="text-align:center;">Lesson 6 - BMI Calculator</h3>  

```python
height = float(input())
weight = float(input())
BMI = int((weight / (height ** 2)))
print(f"{BMI}")
```
<h3 style="text-align:center;">Lesson 7 - Life in Weeks</h3>  

```python
age = int(input())
remaining_age = 90 - age
weeks = int((remaining_age * 52))
print(f"You have {weeks} weeks left.")
```
<h3 style="text-align:center;">Tip Calculator</h3>  

```python
# Tip Calculator
print("Welcome to the tip Calculator")
total_bill = int(input("What is the total bill : "))
tip_percentage = int(input("What is tip percentage : "))
people = int(input("Number of People : "))

total_bill *= (1+(tip_percentage / 100))
per_person = total_bill / people

print(f"Each person should pay : ${'{:.2f}'.format(per_person)}")
print(f"Each person should pay : ${round(per_person, 2)}")
```
