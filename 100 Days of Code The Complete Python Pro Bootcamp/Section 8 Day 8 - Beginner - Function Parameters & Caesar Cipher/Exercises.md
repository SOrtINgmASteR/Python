<h2 style="text-align:center">DAY - 8</h2>  

<h3 style="text-align:center;">Lesson 20 - Paint Area Calculator</h3>  

```python
import math

def paint_calc(height, width, cover):
    no_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {no_of_cans} cans of paint.")

test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
```

<h3 style="text-align:center;">Lesson 21 - Prime Numbers</h3>  

```python
def prime_checker(number):
    if number == 0 or number == 1:
        print("It's not a prime number.")
        return
    elif number == 2:
        print("It's a prime number.")
        return
    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number.")
            return
    print("It's a prime number.")
    return

n = int(input())
prime_checker(number=n)
```  

