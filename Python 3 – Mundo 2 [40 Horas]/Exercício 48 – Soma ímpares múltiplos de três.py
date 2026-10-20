"""

Faça um programa que calcule:
A soma entre todos os números que são múltiplos de três,
e que se encontram no intervalo de 1 até 500.


"""
'''///////////////////////////// MODO 1 /////////////////////////////////'''
s = 0
c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s = s + i
        c = c + 1

print(f"O somátorio de todos os {c} valores foi {s}")


'''///////////////////////////// MODO 2 /////////////////////////////////'''
s = 0
c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        c += 1  # ou, q = q + 1
        s += i  # ou, s = s + c
        print(i, end=" ")
print(f"sao {c} a soma é {s}")



'''///////////////////////////// MODO 3 /////////////////////////////////'''

s = 0
c = 0
for i in range(1, 501):
    if i % 3 == 0:
        if i % 2 != 0:
            s = s + i
            c = c + 1
print(f"São {c} números, somando o total de {s}.")



'''///////////////////////////// MODO 4 /////////////////////////////////'''

s = 0
c = 0
for i in range(3, 501, 6):  # a cada 6 números, 1 é ímpar múltiplo de 3...
    s += i
    c += 1
print(f"a soma dos {c} valores múltiplos de três e ímpares entre 1 e 500 é {s}")
