#1018 - Banknotes
N=int(input())
n=N
n100=int(N//100)
N=N%100
n50=int(N//50)
N=N%50
n20=int(N//20)
N=N%20
n10=int(N//10)
N=N%10
n5=int(N//5)
N=N%5
n2=int(N//2)
N=N%2
n1=N
print(f"{n}")
print(f"{n100} nota(s) de R$ 100,00")
print(f"{n50} nota(s) de R$ 50,00")
print(f"{n20} nota(s) de R$ 20,00")
print(f"{n10} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n2} nota(s) de R$ 2,00")
print(f"{n1} nota(s) de R$ 1,00")
