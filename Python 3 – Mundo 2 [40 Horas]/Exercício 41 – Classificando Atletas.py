'''
programa que leia :

- ano de nascimento de um atleta;

- mostre sua categoria, de acordo com a idade;
     Até 9 anos: MIRIM
     Até 14 anos: INFANTIL
     Até 19 anos: JÚNIOR
     Até 25 anos: SÊNIOR
     Acima de 25 anos: MASTER


'''

from datetime import date

D = date.today().year
N = int(input('Ano de nascimento: '))
I = D - N

if I <= 9:
    print(f'Você tem {I} anos em {D}, sua categoria é MIRIM.')

elif I <= 14: 
    print(f'Você tem {I} anos em {D}, sua categoria é INFANTIL.')

elif I <= 19: 
    print(f'Você tem {I} anos em {D}, sua categoria é JÚNIOR.')

elif I <= 25:
    print(f'Você tem {I} anos em {D}, sua categoria é SÊNIOR.')

elif I > 25:
    print(f'Você tem {I} anos em {D}, sua categoria é MASTER.')