"""

Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.

ex: termo 25 - razao 5 = 25 > 30 > 35 > 40 > 45 > 50 > 55 > 60 > 65 > 70 > FIM DA PA. (a partir do 25 pulando de 5 em 5)
ex: termo 0 - razao 2 = 0 > 2 > 4 > 6 > 8 > 10 > 12 > 14 > 16 > 18 > FIM DA PA. (a partir de 0 pulando de 2 em 2)

aₙ = a₁ + (n − 1) · r

aₙ - primeiro termo
a₁ é o primeiro termo.
n é a posição do termo que você quer calcular.
r é a razão.

Para o 10º termo, n = 10, então o cálculo é a₁ + (10 − 1) · r. 
O primeiro termo já é a₁, então você precisa somar a razão apenas 9 (10-1) vezes para chegar ao 10º.
"""

n = int(input("Primeiro termo: "))
r = int(input("Razão: "))
PA = n + (10 - 1) * r  # 10 termo ,

print("=" * 30)

print(f"10 TERMOS DE UMA PA :")

print("=" * 30)

for i in range(n, PA + r, r):
    print(f"{i}", end=" > ")

print("FIM DA PA.")
