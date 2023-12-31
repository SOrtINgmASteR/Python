<h2 style="text-align:center">DAY - 5</h2>  

<h3 style="text-align:center;">Lesson 16 - Average Height</h3>  

With `range()` function  

```python
heights = input().split(" ")
total = int(0)
for i in range(0, len(heights)):
    heights[i] = int(heights[i])
    total += heights[i]
average = int(round(total / len(heights)))
print(f"total height = {total}")
print(f"number of students = {len(heights)}")
print(f"average height = {average}")
```  
Without `range()` function  

```python
heights = input().split(" ")
total = int(0)
for height in heights:
    total += int(height)
average = int(round(total / len(heights)))
print(f"total height = {total}")
print(f"number of students = {len(heights)}")
print(f"average height = {average}")
```

Lists can be take input also in these ways :   
```
marks = list(map(int, input().split(" ")))
marks = input().split(" ")
marks = [int(mark) for mark in input().split(" ")]
```  
<h3 style="text-align:center;">Lesson 17 - High Score</h3>  

With `range()` function :   

```python
scores = list(map(int, input().split(" ")))
max_score = int(scores[0]);
for i in range(1, len(scores)):
    if scores[i] > max_score:
        max_score = scores[i]
print(f"The highest score in the class is: {max_score}")
```
Without `range()` function :  

```python
scores = list(map(int, input().split(" ")))
max_score = int(scores[0]);
for score in scores:
    if int(score) > max_score:
        max_score = score
print(f"The highest score in the class is: {max_score}")
```
<h3 style="text-align:center;">Lesson 18 - Adding Even Numbers</h3>  

```python
n = int(input())
even_sum = int(0)
for i in range(1, n+1):
    if i % 2 == 0:
        even_sum += i
print(f"{even_sum}")
```

<h3 style="text-align:center;">Lesson 19 - FizzBuzz</h3>  

```python
for i in range(1, 100+1):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(f"{i}")
```

<h3 style="text-align:center;">Password Generator</h3>  

```
my_list = [24, 38, 11, 34, 21, 99, 41]
element = random.choice(my_list)
random.shuffle(my_list)
```

#### Password  Generator (Easy)

```python
# Password Generator - Easy Version
import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""
number_of_letters = int(input("How many letters : "))
number_of_numbers = int(input("How many number : "))
number_of_symbols = int(input("How many symbols : "))

for char in range(0, number_of_letters):
    random_char = random.choice(letters)
    password += random_char
    # print(f"{random_char}", end="")
for number in range(0, number_of_numbers):
    random_num = random.choice(numbers)
    password += str(random_num)
    # print(f"{random_num}", end="")
for symbol in range(0, number_of_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol
    # print(f"{random_symbol}", end="")
print(f"\nPassword = {password}")
```

#### Password  Generator (Hard)

```python
# Password Generator - Hard Version
import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
number_of_letters = int(input("How many letters : "))
number_of_numbers = int(input("How many number : "))
number_of_symbols = int(input("How many symbols : "))

for char in range(0, number_of_letters):
    random_char = random.choice(letters)
    password += random_char
    # print(f"{random_char}", end="")
for number in range(0, number_of_numbers):
    random_num = random.choice(numbers)
    password += str(random_num)
    # print(f"{random_num}", end="")
for symbol in range(0, number_of_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol
    # print(f"{random_symbol}", end="")
random.shuffle(password)

print(f"\nPassword = ", end="")
for i in range(0, len(password)):
    print(f"{password[i]}", end="")
```