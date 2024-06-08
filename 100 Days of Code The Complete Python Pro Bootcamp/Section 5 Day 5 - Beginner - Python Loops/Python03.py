# Exercise - Lesson 16 - Average Height

# With range()
heights = input().split(" ")
total = int(0)
for i in range(0, len(heights)):
    heights[i] = int(heights[i])
    total += heights[i]
average = int(round(total / len(heights)))
print(f"total height = {total}")
print(f"number of students = {len(heights)}")
print(f"average height = {average}")

# Without range()
heights = input().split(" ")
total = int(0)
for height in heights:
    total += int(height)
average = int(round(total / len(heights)))
print(f"total height = {total}")
print(f"number of students = {len(heights)}")
print(f"average height = {average}")

# marks = list(map(int, input().split(" ")))
# marks = input().split(" ")
# marks = [int(mark) for mark in input().split(" ")]
