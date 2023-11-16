# Roller Coaster - 3
print("Welcome to the Roller coaster!")
height = float(input("Enter height in cm : "))
bill = int(0)
if height >= 120.00:
    print("You can ride the Roller coaster")
    age = int(input("Enter your age : "))
    if age < 12:
        bill = 5
        print(f"Child Ticket Price : ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Teen Ticket Price : ${bill}")
    else:
        bill = 12
        print(f"Adult Ticket Price : ${bill}")

    photo = str(input("Do you want a Photograph? 'Y'-yes or 'N'-no : "))
    if photo == "Y":
        print("Photo Price : $3 extra")
        bill += 3
    else:
        print("No Photo Price")

    print(f"Total Bill ${bill}")

else:
    print("Sorry you can't ride the roller coaster")