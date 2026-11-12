"""
Desenvolva um programa que leia o nome, idade e sexo de 4
pessoas. No final do programa, mostre: a média de idade do
grupo, qual é o nome do homem mais velho e quantas mulheres 
tem menos de 20 anos.

"""
tot_idades = 0
nome_homem_velho = ''
maior_idade_homem = 0
menos_vinte = 0
for n in range(1, 5):
    nome = str(input('Qual seu nome? '))
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Você é homem ou mulher? ')).lower()

    tot_idades += idade

    if sexo == 'homem':
        if maior_idade_homem == 0 or idade > maior_idade_homem:
            maior_idade_homem = idade            
            nome_homemVelho = nome

    if sexo == 'mulher' and idade < 20:
        menos_vinte += 1
    
media = tot_idades / 4
    
print('O homem mais velho é o {}'.format(nome_homemVelho))    
print('A idade do {} é de {} anos'.format(nome_homemVelho, maior_idade_homem))
print('A média de todas as idades é {:.0f} anos.'.format(media))
print('{} mulheres têm menos de 20 anos.'.format(menos_vinte))

