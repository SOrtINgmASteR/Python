# Exercise Lesson 17 - High Score

# With range()
scores = list(map(int, input().split(" ")))
max_score = int(scores[0]);
for i in range(1, len(scores)):
    if scores[i] > max_score:
        max_score = scores[i]
print(f"The highest score in the class is: {max_score}")

# Without range()
scores = list(map(int, input().split(" ")))
max_score = int(scores[0]);
for score in scores:
    if int(score) > max_score:
        max_score = score
print(f"The highest score in the class is: {max_score}")
