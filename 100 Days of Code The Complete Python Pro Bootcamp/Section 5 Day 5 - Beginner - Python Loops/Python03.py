# Average Student Marks
# a, b, c, d = map(int, input().split(" "))
marks = input().split(" ")
total = int(1)
for i in range(0, len(marks)):
    marks[i] = int(marks[i])
    total += marks[i]
average = float(total/len(marks))
print(f"Average marks = {'{:.2f}'.format(average)}")
