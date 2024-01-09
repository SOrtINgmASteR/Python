# 1040 - Average 3
s = input().split(" ")
n1, n2, n3, n4 = s
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
gpa = float(((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10)
print(f"Media: {'{:.1f}'.format(gpa)}")

if gpa >= 7.00:
    print("Aluno aprovado.")
elif gpa < 5.00:
    print("Aluno reprovado.")
elif 5.0 <= gpa < 7.00:
    print("Aluno em exame.")
    l = float(input())
    print(f"Nota do exame: {'{:.1f}'.format(l)}")
    gpa2 = (( l + gpa) / 2)
    if(gpa2 >= 5):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {'{:.1f}'.format(gpa2)}")
