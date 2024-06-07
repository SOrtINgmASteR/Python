<h2 style="text-align:center">DAY - 3</h2>  

<h3 style="text-align:center;">Lesson 8 - Odd or Even</h3>  

```python
number = int(input())
if number % 2 == 0:
    print(f"This is an even number.")
else:
    print(f"This is an odd number.")
```
<h3 style="text-align:center;">Lesson 9 - BMI 2.0</h3>  

```python
height = float(input())
weight = float(input())

bmi = (weight/(height ** 2))

print(f"Your BMI is {bmi},", end=" ")
if bmi < 18.5:
    print("you are underweight.")
elif bmi < 25:
    print("you have a normal weight.")
elif bmi < 30:
    print("you are slightly overweight.")
elif bmi < 35:
    print("you are obese.")
else:
    print("you are clinically obese.")
```  
<h3 style="text-align:center;">Lesson 10 - Leap Year</h3>  

**With nested if-else -**  
```python
year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
```  
**With Logical Operator -**  
```python
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not leap year")
```  
<h3 style="text-align:center;">Lesson 11 - Pizza Order Practice</h3>  

```python
bill = int(0)
size = str(input())
if size == "S":
    bill += 15
    pepperoni = str(input())
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    pepperoni = str(input())
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    pepperoni = str(input())
    if pepperoni == "Y":
        bill += 3
extra_cheese = str(input())
if extra_cheese == "Y":
    bill += 1
print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is: ${bill}.")
```  
<h3 style="text-align:center;">another way - </h3>  

```python
bill = int(0)
size = str(input())
if size == 'L':
    bill += 25
elif size == 'M':
    bill += 20
elif size == 'S':
    bill += 15

pepperoni = str(input())
if pepperoni == 'Y':
    if size == 'M' or size == 'L':
        bill += 3
    elif size == 'S':
        bill += 2

extra_cheese = str(input())
if extra_cheese == 'Y':
    bill += 1

print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is: ${bill}.")
```

<h3 style="text-align:center;">Lesson 12 - Love calculator</h3>  

```python
name1 = str(input())
name2 = str(input())
combined_name = name1 + name2
combined_name = combined_name.lower()

t = int(combined_name.count("t"))
r = int(combined_name.count("r"))
u = int(combined_name.count("u"))
e = int(combined_name.count("e"))
first_digit = str((t + r + u + e))

l = int(combined_name.count("l"))
o = int(combined_name.count("o"))
v = int(combined_name.count("v"))
e = int(combined_name.count("e"))
second_digit = str((l + o + v + e))

score = int(first_digit + second_digit)

print("The Love Calculator is calculating your score...")

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
```  
<h3 style="text-align:center;">Treasure Island</h3>  

```python
print("WELCOME TO THE TREASURE ISLAND!")
left_or_right = str(input("Where do you want to go? left or right : "))
if left_or_right == "left":
    swim_or_wait = str(input("There is a river ahead of you! Do you want to swim or wait : "))
    if swim_or_wait == "wait":
        red_or_blue = str(input("Found two doors! Which door you want to go in? red or blue or yellow: "))
        if red_or_blue == "blue":
            print("Eaten by beasts!!!")
            print("Game Over")
        elif red_or_blue == "red":
            print("Burned by fire!!!")
            print("Game Over!")
        elif red_or_blue == "yellow":
            print("You Win!!!")
    else:
        print("Attacked by trout!!!")
        print("Game Over!")
else:
    print("Fall in to a hole!!!")
    print("Game Over!")
```