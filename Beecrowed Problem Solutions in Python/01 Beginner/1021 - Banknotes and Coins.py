#1021 - Banknotes and Coins
N=float(input())
n=N
n100=int(N//100)
N-=(n100*100)
n50=int(N//50)
N-=(n50*50)
n20=int(N//20)
N-=(n20*20)
n10=int(N//10)
N-=(n10*10)
n5=int(N//5)
N-=(n5*5)
n2=int(N//2)
N-=(n2*2)
n1=int(N//1)
N-=(n1*1)
N*=100
np50=int(N//50)
N-=(np50*50)
np25=int(N//25)
N-=(np25*25)
np10=int(N//10)
N-=(np10*10)
np5=int(N//5)
N-=(np5*5)
np1=int(N)

print("NOTAS:")
print(f"{n100} nota(s) de R$ 100.00")
print(f"{n50} nota(s) de R$ 50.00")
print(f"{n20} nota(s) de R$ 20.00")
print(f"{n10} nota(s) de R$ 10.00")
print(f"{n5} nota(s) de R$ 5.00")
print(f"{n2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{n1} moeda(s) de R$ 1.00")
print(f"{np50} moeda(s) de R$ 0.50")
print(f"{np25} moeda(s) de R$ 0.25")
print(f"{np10} moeda(s) de R$ 0.10")
print(f"{np5} moeda(s) de R$ 0.05")
print(f"{np1} moeda(s) de R$ 0.01")
