<h2 style="text-align:center">DAY - 1</h2>  

<h3 style="text-align:center;">Lesson 1 - Printing</h3>    

**Using separate `print()` function for each line :**  
```python
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
```
**Using a single `print()` function for all the lines :**
```python
print('''Day 1 - Python Print Function
The function is declared like this:
print('what to print')
''')
```

<h3 style="text-align:center;">Lesson 2 - Debugging Practise</h3>   

**Find errors-**
```
print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")
```
**Errors-**  
1.In the first line the beginning `"` is missing.  
2.In second line an extra '+' need to be added for the desired output.  
3.In the third line extra indentation was used.  
4.In the fourth line an extra bracket is used.  
**Code without Errors-**  
```python
print("Day 1 - String Manipulation")
print('String Concatenation is done with the ' + '"+"' + ' sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
```
<h3 style="text-align:center;">Lesson 3 - Input Function</h3>  

<h4 style="text-align:center">Exercise - 1</h4>    

```python
num1 = int(input())
num2 = int(input())
print(num1 * num2)
```
<h4 style="text-align:center">Exercise - 2</h4>  

```python
s = input()
length = len(s)
print(length)
```
<h3 style="text-align:center;">Lesson 4 - Variables</h3>  

<h4 style="text-align:center">Exercise - 1</h4>  

We will just swap the variables -  
Input - 
```
a = input()
b = input()
```
Swapping variables - 
```
temp = a
a = b
b = temp
```
Printing - 
```
print("a: " + a)
print("b: " + b)
```
<h4 style="text-align:center">Exercise - 2 Band Name Generator</h4>  

```python
city_name = str(input("Enter your city name : "))
pet_name = str(input("Enter your pet name : "))
band_name = str(city_name + " " + pet_name)
print(f"Your Band Name : {band_name}")
```
