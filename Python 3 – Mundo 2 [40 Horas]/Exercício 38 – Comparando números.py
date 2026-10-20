''' 


Um programa que leia 2 números inteiros e compare-os mostrando:
- O primeiro valor é MAIOR
- O segundo valor é MAIOR
- NAO EXISTE valor maior, sao IGUAIS.


'''

N1 = int(input('Digite um número: '))
N2 = int(input('Digite um número: '))

if N1 > N2:
    print(f'O primeiro valor {N1} é maior que {N2}')
elif N2 > N1:
    print(f'O segundo valor {N2} é maior que {N1}')
elif N2 == N1:
    print(f'Os valores de {N1} e {N2} são IGUAIS!')
