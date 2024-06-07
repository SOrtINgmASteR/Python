# Roller Coaster -2

print("Welcome to the Roller coaster!")
height = float(input("Enter height in cm : "))
if height >= 120.00:
    print("You can ride the Roller coaster.")
    age = int(input("Enter your age : "))
    if age < 12:
        print("Pay $5")
    elif age <= 18:
        print("Pay $7")
    elif age <= 22:
        print("Pay $10")
    else:
        print("Pay $12")
else:
    print("Sorry you can't ride the roller coaster.")
