'''
Refaça o DESAFIO 9:
mostrando a tabuada de um número que o usuário escolher, 
só que agora utilizando um laço for.


'''

n = int(input('Digite um Número: '))

print('=' * 30)

print(f'TABUADA DE {n} :')

print('=' * 30)

for c in range(0,11):
    
    print(f'{n} x {c} = {n*c}')

print('=' * 30)


'''///////////////////// MODO2 /////////////////////////////'''

n = int(input('Digite um Número: '))
L = int(input('Até qual número? '))

print('=' * 30)

print(f'TABUADA DE {n} :')

print('=' * 30)

for c in range(0,L+1):
    
    print(f'{n} x {c} = {n*c}')

print('=' * 30)