# Exercise - Lesson 18 - Adding Even Numbers

n = int(input())
even_sum = int(0)
for i in range(1, n+1):
    if i % 2 == 0:
        even_sum += i
print(f"{even_sum}")
