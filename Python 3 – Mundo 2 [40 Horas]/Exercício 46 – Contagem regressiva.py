"""

Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
indo de 10 até 0, com uma pausa de 1 segundo entre eles.

"""

from time import sleep

for c in range(
    10, -1, -1
):  # 10 ate 0 decrescente, se quiser numero negativo continuar diminuindo o do meio
    print(c)
    sleep(2)
print("BUM! BUM! POOW! FELIZ ANO NOVO!!! ")
