# Exercise - Lesson 14 - Banker Roulette

import random
# friends = input().split(", ")
friends = list(map(str, input().split(", ")))
length = int(len(friends))
index = int(random.randint(0, length - 1))
print(f"{friends[index]} is going to buy the meal today!")
