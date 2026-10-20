'''
Programa para aprovar emprestimo bancário para comprar uma casa.

Prestaçao mensal nao pode exceder 30% do salário. (30% = 0.30)

Perguntar: 
- Valor da casa
- Salário
- Quantos anos vai pagar (quantidade de prestaçoes)

'''


C = float(input('Valor da casa: R$ '))
S = float(input('Valor do salário: R$ '))
A = int(input('Quantos anos de financiamento? '))

P = C / (A * 12)  # valor da casa (C) dividido pela Anos (A) a pagar (A * 12) transformando em meses = PRESTAÇAO

M = S * 30 / 100 # S * 0.30 - excedente (30% do salario(S)) = MINIMO (M)

# print(f'COMPARANDO tem que pagar R${P:.2f} e o minimo é de R${M:.2f}')


print(f'Para pagar uma casa de R$ {C:.2f} em {A} anos.', end=' ')
print(f'A prestação será de R${P:.2f}')

if P <= M : # PRESTACAO(P) TEM QUE SER IGUAL OU MENOR QUE 30% DO SALARIO (M)
    print('Empréstimo APROVADO!')

else:
    print('Empréstimo NEGADO!')
