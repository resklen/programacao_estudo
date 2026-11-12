"""
Faça um programa que receba um número real, encontre e mostre:

a) a parte inteira desse número;
b) a parte fracionária desse número;
c) o arredondamento desse número.

"""
from math import modf
real = float(input('Digite um número real: '))

parte_fracionaria, parte_inteira = modf(real)

print(f'A parte inteira do número {real} é: {parte_inteira:.0f}')
print(f'A parte fracionária do número {real} é {parte_fracionaria}')
print(f'O número {real} pode ser arredondado para {round(real)}')
