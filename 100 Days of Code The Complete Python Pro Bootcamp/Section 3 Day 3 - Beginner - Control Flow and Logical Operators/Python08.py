# Pizza Price
bill = int(0)
size = str(input("Which Pizza size do you want? L, M, S : "))
if size == "S":
    bill = 15
    pepperoni = str(input("Add pepperoni for small? Y-yes or N-no : "))
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    pepperoni = str(input("Add pepperoni for medium or large? Y-yes or N-no : "))
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    pepperoni = str(input("Add pepperoni for medium or large? Y-yes or N-no : "))
    if pepperoni == "Y":
        bill += 3
extra_cheese = str(input("Add Extra Cheese for any pizza? Y-yes or N-no : "))
if extra_cheese == "Y":
    bill += 1
print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is ${bill}.")