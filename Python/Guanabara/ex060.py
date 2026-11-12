"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.

"""

# numero = int(input('Digite um número para saber seu fatorial: '))
# n = 1
# while n != numero:
#     fatorial = numero * n   
#     n = numero - 1
#     print(fatorial)

# from math import factorial
# n = int(input('Digite um número para calcular seu fatorial: '))
# f = factorial(n)
# print('O fatorial de {} é {}'.format(n, f))

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
