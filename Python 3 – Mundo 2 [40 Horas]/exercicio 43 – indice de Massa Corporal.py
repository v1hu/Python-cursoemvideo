'''
- Peça : PESO e ALTURA;

- Calcule o Indice de Massa Corporal (IMC)  = imc = peso / (altura ** 2);

- Mostre o STATUS:
   Abaixo de 18,5: Abaixo do Peso
   Entre 18,5 e 25: Peso Ideal
   Entre 25 até 30: Sobrepeso
   Entre 30 até 40: Obesidade
   Acima de 40: Obesidade Mórbida

'''

P = float(input('Digite o peso: (Kg)  '))
A = float(input('Digite a altura: (Metros) '))

IMC = P / (A ** 2)

if IMC <= 18.5:
    print(f'Você tem {P}Kg e {A} de altura, seu IMC é {IMC:.1f}, ABAIXO DO PESO!')

elif IMC <= 25:
    print(f'Você tem {P}Kg e {A} de altura, seu IMC é {IMC:.1f}, PESO IDEAL!')

elif IMC <= 30:
    print(f'Você tem {P}Kg e {A} de altura, seu IMC é {IMC:.1f}, SOBREPESO!')

elif IMC <= 40:
    print(f'Você tem {P}Kg e {A} de altura, seu IMC é {IMC:.1f}, OBESIDADE!')

elif IMC >= 40:
    print(f'Você tem {P}Kg e {A} de altura, seu IMC é {IMC:.1f}, OBESIDADE MÓRBIDA!')