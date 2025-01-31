# Exercício 04) Verificação de número par ou ímpar

print(" -> NÚMERO PAR OU ÍMPAR <- ")
num1 = int(input("Digite o número: "))

if num1 % 2 == 0:
    print(f"O número {num1} é par.")
else:
    print(f"O número {num1} é ímpar.")