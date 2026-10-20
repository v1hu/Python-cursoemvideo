'''
Calcule o valor a ser pago por um produto considerando seu preço normal e a condiçao de pgto.
 
 Condição de pagamento.

 - à vista dinheiro/cheque: 10% de desconto; 0 

 – à vista no cartão: 5% de desconto; 1

 – Até 2x no cartão: preço formal; 2

 – 3x ou mais no cartão: 20% de juros; 3

'''

V = float(input('Qual valor do produto? R$ '))

print('A VISTA DINHEIRO OU CHEQUE (0) - A VISTA CARTAO (1) - PARCELADO 2x (2) - PARCELADO 3x ou mais (3)')

P = int(input('Número de parcelas? '))

if P == 0:
    print(f'O valor do produto é {V:.2f}R$, À VISTA (DINHEIRO/CHEQUE/PIX) com 10% de desconto, {V - (V * 10/100 ):.2f}')

elif P == 1:
    print(f'O valor do produto é {V:.2f}R$, À VISTA NO CARTÃO com 5% de desconto, {V - (V * 10/100 ):.2f} ')

elif P == 3:
    print(f'O valor do produto é {V:.2f} R$, Parcelado em 3x ou mais com 20% de juros, {V + (V * 20/100 ):.2f} R$ ')

elif P == 2:
    print(f'O valor do produto parcelado em até 2x no CARTÃO é {V:.2f} R$')