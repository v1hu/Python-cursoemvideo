'''

Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade:

- se ele ainda vai se alistar ao serviço militar;
- se é a hora exata de se alistar ou se já passou do tempo do alistamento. 

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

'''

from datetime import date

D = date.today().year

N = int(input('Ano de nascimento: '))

I = D - N

print(f'Quem nasceu em {N} tem {I} anos em {D}.')

if I == 18:
    print(f'Você tem {I} anos deve se alistar IMEDIATAMENTE!')

elif I < 18:
    print(f'Você tem {I} anos, ainda falta {18 - I} anos para o alistamento!')
    print(f'Seu alistamento será em {D + 18 - I}.')

elif I > 18:
    print(f'Você tem {I} anos, ja passou {I - 18} anos, ja deveria ter se alistado! ')
    print(f'Seu alistamento foi em {D - I + 18}.')