# Exercise - Lesson 9 - BMI 2.0

height = float(input("Enter your height in meters : "))
weight = float(input("Enter your weight in K.G : "))
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
