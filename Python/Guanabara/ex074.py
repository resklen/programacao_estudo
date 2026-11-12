"""
Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla. Depois disso, mostre a listagem de números gerados
e também indique o maior e o menor valor que estão na tupla.

"""
from random import randint
primeiro = randint(0, 9)
segundo = randint(0, 9)
terceiro = randint(0, 9)
quarto = randint(0, 9)
quinto = randint(0, 9)

numeros = (primeiro, segundo, terceiro, quarto, quinto)
#print(f'Eu sorteei os números: {numeros}')
maior = max(numeros)
menor = min(numeros)

print('Os números sorteados foram: ', end='')
for n in numeros:
    
    print(n, end=' ')

print(f'\nO maior número é o {maior}. ')
print(f'O menor número é o {menor}. ')
