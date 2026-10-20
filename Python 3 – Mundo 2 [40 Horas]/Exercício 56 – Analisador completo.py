"""

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo;
- qual é o nome do homem mais velho;
- e quantas mulheres têm menos de 20 anos.


"""

SI = 0  # SOMA IDADE
MI = 0  # MEDIA IDADE
MIH = 0  # MAIOR IDADE HOMEM
NV = ""  # NOME DO MAIS VELHO
M20 = 0  # MULHER 20 ANOS

for P in range(1, 5):  # P = pessoas
    print(f"===== {P}ºPESSOA =====")

    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F] ")).strip()
    SI += idade
    
    if P == 1 and sexo in "Mm":  # se a pessoa for a primeira pessoa e sexo masculino
        MIH = idade
        NV = nome
    
    if sexo in "Mm" and idade > MIH:  #qual é o nome do homem mais velho;
        MIH = idade
        NV = nome
   
    if sexo in "Ff" and idade < 20: #quantas mulheres têm menos de 20 anos
        M20 += 1

MI = SI / 4 # A média de idade do grupo

print(f"A média de idade do grupo é de {MI:.2f} anos")
print(f"O homem mais velho tem {MIH} anos e se chama {NV}.")
print(f"A o todo são {M20} mulheres com menos de 20 anos. ")
