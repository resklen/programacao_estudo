"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o
usuário quer ou não continuar. No final mostre:

A) Quantas pessoas tem mais de 18 anos

B) Quantos homens foram cadastrados

C) Quantas mulheres tem menos de 20 anos.

"""
i = 0
h = 0
m = 0
while True:
    idade = int(input('Digite sua idade: '))
    
    if idade >= 18:
        i += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Você pertence ao sexo [M]asculino ou [F]eminino? ')).strip().upper()[0]
    if sexo in 'M':
        h += 1 
    elif sexo in 'F' and idade < 20:
        m += 1
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]

    if continuar in 'S':
        continue
    else:
        break

print(f'Pessoas com mais de 18 anos: {i}')
print(f'Homens cadastrados: {h}')
print(f'Mulheres com menos de 20 anos: {m}')
 