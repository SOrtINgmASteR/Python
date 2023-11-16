#1046 - Game Time
start, finish = map(int, input().split(" "))
duration=int(finish-start)
if duration<=0:
    duration+=24
print(f"O JOGO DUROU {duration} HORA(S)")
