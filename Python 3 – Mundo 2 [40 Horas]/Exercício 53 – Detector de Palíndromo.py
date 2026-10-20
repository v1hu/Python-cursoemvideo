'''

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Exemplos de palíndromos:

- APÓS A SOPA, 
- A SACADA DA CASA, 
- A TORRE DA DERROTA, 
- O LOBO AMA O BOLO, 
- ANOTARAM A DATA DA MARATONA.

'''

F = str(input('Digite uma frase: ')).strip().upper() # tirar os espaços entre as palavras antes e depois (strip) , # maiusculo para n ter problema de comparaçao (upper) - F = frase

P = F.split() # separar as palavras em lista = P = palavras = Você digitou a frase ['CURSO', 'EM', 'VIDEO', 'DE', 'PYTHON'] = coleçoes / lista

J = ''.join(P) # Juntar as palavras desconsiderando os espaços ''.join(P) = J = Você digitou a frase CURSOEMVIDEODEPYTHON // CURSO*EM*VIDEO*DE*PYTHON = J = '*'.join(P)

I = ''  # inverso

for L in range(len(J) - 1, -1, -1 ):  # L = Letra //  Vai começar len(J) - 1, números de letras -1 // Letra -1 antes da primeira letra que é zero // e volta 1 letra = -1
   
    I += J[L]

print(f'O inverso de {J} é {I}')

if I == J:
    print(f'A frase digitada foi {F}, Temos um PALÍNDROMO!')

else:
    print(f'A frase digitada foi {F}, não é um PALÍNDROMO!')





'''/////////////////  MODO 2  /////////////////////////'''

F = str(input('Digite uma frase: ')).strip().upper() 

P = F.split() 

J = ''.join(P) 

I = J[::-1] # fatiamento

print(f'O inverso de {J} é {I}')

if I == J:
    print(f'A frase digitada foi {F}, Temos um PALÍNDROMO!')

else:
    print(f'A frase digitada foi {F}, não é um PALÍNDROMO!')