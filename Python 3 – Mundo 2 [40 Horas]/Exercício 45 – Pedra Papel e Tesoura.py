''' Crie um programa que faça o computador jogar Jokenpô com você.'''

import random
from time import sleep

G = ['PEDRA ✊', 'PAPEL ✋' ,'TESOURA ✌️']
C = random.choice(G)

print('''
===== PEDRA , PAPEL e TESOURA =====

[ 1 ] - PEDRA ✊
[ 2 ] - PAPEL ✋
[ 3 ] - TESOURA ✌️

''')
J = int(input(f'{ ' ESCOLHA SUA JOGADA! ':=^40}\n'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

if J == 1:
    J = 'PEDRA ✊'

elif J == 2:
    J = 'PAPEL ✋'

elif J == 3:
    J = 'TESOURA ✌️'

else:
    print('OPÇÃO INVÁLIDA!')

print(f'Você escolheu: {J}')
print(f'O computador escolheu: {C}')

if J == C:
    print('EMPATE! 😂❤️‍🔥')

elif J == 'PEDRA ✊' and C == 'TESOURA ✌️':
    print('VOCÊ VENCEU! 🎉🏅')

elif J == 'TESOURA ✌️' and C == 'PAPEL ✋':
    print('VOCÊ VENCEU! 🎉🏅')

elif J == 'PAPEL ✋' and C == 'PEDRA ✊':
    print('VOCÊ VENCEU! 🎉🏅')

else:
    print('VOCÊ PERDEU! 👎❌')
