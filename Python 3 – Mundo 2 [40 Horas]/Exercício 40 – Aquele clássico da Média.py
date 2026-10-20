'''

Crie um programa que leia duas notas de um aluno e calcule sua média e mostre uma mensagem:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO

'''

N1 = float(input('Nota da P1: '))
N2 = float(input('Nota da P2: '))

M = (N1+N2)/2

if M < 5:
    print(f'Sua média foi {M:.2f}, REPROVADO!')

elif 5 <= M < 6.9: # elif M >= and M < 7
    print(f'Sua média foi {M:.2f}, RECUPERAÇÃO!')

elif M >= 7:
    print(f'Sua média foi {M:.2f}, APROVADO!')
