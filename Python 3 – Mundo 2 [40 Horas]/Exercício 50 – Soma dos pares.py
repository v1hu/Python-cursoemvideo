"""
Desenvolva um programa que leia seis números inteiros:
- Mostre a soma apenas daqueles que forem pares.
- Se o valor digitado for ímpar, desconsidere-o.

"""

''' ///////////////// MODO 1 PARES //////////////////////'''


s = 0
c = 0
for i in range(1,7):
    n = int(input(f"Digite o {i}º número: "))
    if n % 2 == 0:  # só soma se for par
        s += n  # ímpares são ignorados
        c += +1
print(f" Você informou {c} números PARES, e a soma dos valores foi {s}")



''' ///////////////// MODO 2 IMPARES //////////////////////'''

s = 0
c = 0
for i in range(6):
    n = int(input(f"Digite o {i + 1}º número: "))
    if n % 2 != 0:  # ímpar: resto 1 na divisão por 2
        s += n
        c += +1

print(f"Você informou {c} números ÍMPARES, e a soma dos valores foi {s}")