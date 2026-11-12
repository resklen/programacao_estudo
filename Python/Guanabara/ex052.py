"""
Faça um programa que leia um número inteiro e diga se ele é um número
primo ou não.

"""
from math import sqrt
num = int(input('Digite um número inteiro: '))

nvezes = 0

for c in range(1, num + 1):

    if num % c == 0:
        print('\33[1;32m', end='')
        nvezes += 1
    else:
        print('\33[1;31m', end='')
    print('{}\33[m '.format(c), end='')
print('\nO número {} foi divisível {} vezes.'.format(num, nvezes))

if nvezes <= 2:
    print('Portanto, número {} é primo.'.format(num))
else:
    print('Portanto, número {} não é primo.'.format(num))
    