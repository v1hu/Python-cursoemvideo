''' 

Programa que leia um número inteiro qualquer,
peça para o usuário escolher qual será a base de conversão:

- 1 para BINÁRIO - :b - binário {N:b}

- 2 para OCTAL - :o - octal {N:o}

- 3 para HEXADECIMAL
    :x - hexadecimal com letras minúsculas {N:x}
    :X - hexadecimal com letras maiúsculas {N:X}

'''



N = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão: 
[ 1 ] - Converter para BINÁRIO :
[ 2 ] - Converter para OCTAL :
[ 3 ] - Converter para HEXADECIMAL :
''')
O = int(input('Sua opção: '))

if O == 1:
    print(f'O número transformado em Binário é: {N:b}') # ex:320 = bin(320) = resposta = 0b101000000 = ab = binário = sem o prefixo = bin(N)[2:]

elif O == 2:
    print(f'O número transfomado em Octal é: {N:o}') # ex:360 = oct(360) = resposta = 0o550 = 0o = octal = oct(N)[2:]

elif O == 3:
    print(f'O número transformado em Hexadecimal é: {N:x}') # ex:141 = hex(141) = resposta = 0x8d = 0x = hexadecimal = hex(N)[2:]

else:
    print('Opção INVÁLIDA!')