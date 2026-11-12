"""
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.

"""
maior_peso = 0
menor_peso = 0

for n in range(1, 6):
    peso = float(input('Digite a massa em kg da {}ª pessoa: '.format(n)))

    if n == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
      
    print('Maior peso até agora = {}'.format(maior_peso))
    print('Menor peso até agora = {}'.format(menor_peso))
print('A maior massa é {}kg'.format(maior_peso))
print('A menor massa é {}kg'.format(menor_peso))
    