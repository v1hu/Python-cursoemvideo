'''

Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.


'''

PMA = 0 #Maior peso
PME = 0 #Menor peso

for P in range(1,6): # P = pessoas
        
    peso = float(input(f'Qual o peso da {P}º pessoa : ')) 

    if P == 1: # peso da primeira pessoa
        PMA = peso # menor peso = peso
        PME = peso # maior peso = peso

    else: #se nao for o primeiro laço
        if peso > PMA : # se o peso lido for maior que o peso que eu tenho
            PMA = peso # se o maior peso for maior que o primeiro peso, ele passa a ser o maior
        if peso < PME:
            PME = peso

print(f'O maior peso lido foi {PMA}Kg, e o menor peso foi {PME}Kg.')
