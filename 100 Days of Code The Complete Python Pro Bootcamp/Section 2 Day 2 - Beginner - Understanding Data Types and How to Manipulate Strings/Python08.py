#Tip Calculator
print("Welcome to the tip Calculator")
total_bill = int(input("What is the total bill : "))
tip_percentage = int(input("What is tip percentage : "))
people = int(input("Number of People : "))

total_bill *= (1+(tip_percentage/100))
per_person = total_bill / people

print(f"Each person should pay : ${'{:.2f}'.format(per_person)}")
