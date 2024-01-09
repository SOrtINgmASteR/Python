# 1061 - Event Time
dia, day1 = input().split(" ")
hour1, minute1, second1 = map(int, input().split(":"))
dia, day2 = input().split(" ")
hour2, minute2, second2 = map(int, input().split(":"))
day1 = int(day1)
day2 = int(day2)

day = day2 - day1
hour = hour2 - hour1
minute = minute2 - minute1
second = second2 - second1

if second < 0:
    second += 60
    minute -= 1
if minute < 0:
    minute += 60
    hour -= 1
if hour < 0:
    hour += 24
    day -= 1

print(f"{day} dia(s)")
print(f"{hour} hora(s)")
print(f"{minute} minuto(s)")
print(f"{second} segundo(s)")
