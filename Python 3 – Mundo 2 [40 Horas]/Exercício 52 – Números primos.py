"""

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

número primo = divisivel 2 vezes, por 1 e por ele mesmo.

"""

n = int(input("Digite um número: "))

d = 0  # numero de divisiveis

for c in range(1, n + 1):

    if n % c == 0:  # se o numero for divisivel = vermelho

        print("\033[31m", end="")
        d += 1

    else:

        print("\033[33m", end="")  # se n for divisivel = verde

    print(f"{c}", "\033[m", end=" ")

print(f"\nO número \033[33m{c}\033[m foi divisivel \033[33m{d}\033[m vezes ")

if d == 2:
    print("E por isso ele é \033[31mPRIMO!\033[m")

else:
    print("E por isso ele \033[31mNÃO\033[m é \033[31mPRIMO!\033[m")
