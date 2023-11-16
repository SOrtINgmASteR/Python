# BMI interpretation
height = float(input("Enter your height in Meter : "))
weight = float(input("Enter your weight in K.G. : "))
bmi = (weight/(height ** 2))
print(f"Your BMI is : {'{:.2f}'}.".format(bmi), end=" ")
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25 :
    print("You have normal weight.")
elif bmi < 30 :
    print("You are slightly overweight.")
elif bmi < 35 :
    print("You are obese.")
else :
    print("You are clinically overweight.")