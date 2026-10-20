'''
Calcule o valor a ser pago por um produto considerando seu preço normal e a condiçao de pgto.
 
 Condição de pagamento.

 - à vista dinheiro/cheque: 10% de desconto;

 – à vista no cartão: 5% de desconto;

 – Até 2x no cartão: preço formal;

 – 3x ou mais no cartão: 20% de juros;

'''
print(f'{ ' SUPER MERCADOS GUANABARA ':=^40}')

V = float(input('Valor total das compras: R$ '))

print('''Escolha a forma de pagamento: 
[ 1 ] - VISTA DINHEIRO/CHEQUE/PIX - 10% Desconto
[ 2 ] - VISTA NO CARTÃO - 5% Desconto
[ 3 ] - ATÉ 2x NO CARTÃO
[ 4 ] - PARCELADO NO CARTÃO 3x - 20% Juros
''')

O = int(input('Sua opção: '))

if O == 1:
    print(f'O valor das compras é R${V:.2f}, À VISTA (DINHEIRO/CHEQUE/PIX) com 10% de desconto, R${V - (V * 10/100 ):.2f}')

elif O == 2:
    print(f'O valor das compras é R${V:.2f}, À VISTA NO CARTÃO com 5% de desconto, {V - (V * 5/100 ):.2f} ') 

elif O == 3:
    print(f'O valor das compras parcelado em até 2x no CARTÃO é R${V:.2f} cada parcela vai ser R${V/2:.2f}')

elif O == 4:
    P = int(input('Quantas pacelas? '))
    print(f'O valor das compras é R${V:.2f}, Parcelado em {P}x com 20% de juros R${V + (V * 20/100 ):.2f}. ')
    print(f'Sua compra será parcelada em {P}x de R${(V + (V * 20/100 )) / P:.2f}')

else:
    print(f'{' OPÇÃO INVÁLIDA, TENTE NOVAMENTE! ':=^40}')