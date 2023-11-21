# Exercise - who will pay the bill
import random
friends = ["Tausif", "Mesbah", "Sharif", "Ovi", "Priom", "Sourav", "Faisal"]
list_length = int(len(friends))
index = random.randint(0, (list_length-1))
print(f"{friends[index]} will pay the bills.")
