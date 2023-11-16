# Love Calculator
name1 = str(input("Enter 1st Name : "))
name2 = str(input("Enter 2nd Name : "))
combined_name = name1 + name2
combined_name = combined_name.lower()

t = int(combined_name.count("t"))
r = int(combined_name.count("r"))
u = int(combined_name.count("u"))
e = int(combined_name.count("e"))
first_digit = str((t + r + u + e))

l = int(combined_name.count("l"))
o = int(combined_name.count("o"))
v = int(combined_name.count("v"))
e = int(combined_name.count("e"))
second_digit = str((l + o + v + e))

score = int(first_digit + second_digit)
print(f"Your score is {score}, ", end="")

if (score < 10) or (score > 90):
    print("you go together with coke & mentos.")
elif 40 <= score <= 50:
    print("you are alright together.")