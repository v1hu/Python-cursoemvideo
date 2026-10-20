'''
 Refaça o DESAFIO 35 dos triângulos:
 
 acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes

'''
L1 = float(input('Qual a primeira medida do triângulo: '))
L2 = float(input('Qual a primeira medida do triângulo: '))
L3 = float(input('Qual a primeira medida do triângulo: '))

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print("Os segmentos acimda formam um TRIÂNGULO" ,end=' ')
    if L1 == L2 == L3:
        print('EQUILÁTERO.')
    elif L1 != L2 != L3 != L1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print("Os segmentos acima NÃO FORMAM UM TRIÂNGULO")