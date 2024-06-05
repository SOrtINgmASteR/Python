<h2 style="text-align:center">DAY - 1</h2>  

<h3 style="text-align:center;">Lesson 1 - Printing</h3>    

**Using separate `print()` function for each line :**  
```python
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")
```  

**Using a single `print()` function for all the lines :**  
```python
print('''1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
2. Knead the dough for 10 minutes.
3. Add 3g of Salt.
4. Leave to rise for 2 hours.
5. Bake at 200 degrees C for 30 minutes.
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
- In the first line the beginning `"` is missing.  
- In second line an extra '+' need to be added for the desired output.  
- In the third line extra indentation was used.  
- In the fourth line an extra bracket is used.  

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
<h3 style="text-align:center">Band Name Generator</h3>  

```python
city_name = str(input("Enter your city name : "))
pet_name = str(input("Enter your pet name : "))
band_name = str(city_name + " " + pet_name)
print(f"Your Band Name : {band_name}")
```
