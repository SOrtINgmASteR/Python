# Exercise - Lesson 10 - Leap Year
year = int(input("Enter year : "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")
