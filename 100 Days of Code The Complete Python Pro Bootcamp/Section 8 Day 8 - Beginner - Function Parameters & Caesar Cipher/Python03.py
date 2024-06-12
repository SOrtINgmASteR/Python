# Exercise - Lesson 20 - Paint Area Calculator
import math


def paint_calc(height, width, cover):
    no_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {no_of_cans} cans of paint.")


test_h = int(input("Enter Height : "))
test_w = int(input("Enter Width : "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
