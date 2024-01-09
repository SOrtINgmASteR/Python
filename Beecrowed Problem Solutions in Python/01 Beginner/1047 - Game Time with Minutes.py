# 1047 - Game Time with Minutes
h1, m1, h2, m2 = map(int, input().split(" "))
if h1 == h2 and m1 == m2 :
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else :
    M = int(m2 - m1)        
    H = int(h2 - h1)
    if M < 0:
        M += 60
        H -= 1
    if H < 0:
        H += 24
    print(f"O JOGO DUROU {H} HORA(S) E {M} MINUTO(S)")
