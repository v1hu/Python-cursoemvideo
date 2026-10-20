''' 

Crie um programa que faça o computador jogar Jokenpô com você.
molde curso em video

'''

from random import randint
import select
from time import sleep

G = ('PEDRA ✊', 'PAPEL ✋' ,'TESOURA ✌️')
C = randint(0,2)

print('''
===== PEDRA , PAPEL e TESOURA =====

[ 0 ] - PEDRA ✊
[ 1 ] - PAPEL ✋
[ 2 ] - TESOURA ✌️

''')
print('-='*20)

J = int(input(f'{ ' ESCOLHA SUA JOGADA! ':^40}\n'))

if J < 0 or J > 2:
    print('❌ OPÇÃO INVÁLIDA! ❌')
    raise SystemExit

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-='*20)

print(f'JOGADOR: {G[J]}')

print(f'COMPUTADOR: {G[C]}')

print('-='*20)


if C == 0:
    if J == 0:
        print(f'{'EMPATE! 😎🏆🤖':^40}')
        print('-='*20)
    elif J == 1:
        print(f'{'VOCÊ VENCEU! 😎🏆':^40}')
        print('-='*20)
    elif J == 2:
        print(f'{'COMPUTADOR VENCEU! 🤖🏆':^40}')
        print('-='*20)
    else:
        print(f'{'❌ OPÇÃO INVÁLIDA! ❌':^40}')
        print('-='*20)

elif C == 1:
    if J == 0:
        print(f'{'COMPUTADOR VENCEU! 🤖🏆':^40}')
        print('-='*20)
    elif J == 1:
        print(f'{'EMPATE! 😎🏆🤖':^40}')
        print('-='*20)
    elif J == 2:
        print(f'{'VOCÊ VENCEU! 😎🏆':^40}')
        print('-='*20)
    else:
        print(f'{'❌ OPÇÃO INVÁLIDA! ❌':^40}')
        print('-='*20)

elif C == 2:
    if J == 0:
        print(f'{'VOCÊ VENCEU! 😎🏆':^40}')
        print('-='*20)
    elif J == 1:
        print(f'{'COMPUTADOR VENCEU! 🤖🏆':^40}')
        print('-='*20)
    elif J == 2:
        print(f'{'EMPATE! 😎🏆🤖':^40}')
        print('-='*20)
    else:
        print(f'{'❌ OPÇÃO INVÁLIDA! ❌':^40}')
        print('-='*20)
