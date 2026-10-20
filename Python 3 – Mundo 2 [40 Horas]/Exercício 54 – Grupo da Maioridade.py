'''

Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


'''
from datetime import date
A = date.today().year # data atual
TMA = 0 #total maior de idade
TME = 0 #total menor de idade

for P in range(1,8):
        
    N = int(input(f'Ano de nascimento da {P}º pessoa : ')) # nascimento
    
    I = A - N # atual - nascimento

    if I >= 18:
        TMA += 1

    else:
        TME += 1

print(f'Ao todo tivemos {TMA} pessoas maiores e {TME} menores de idade. ')
