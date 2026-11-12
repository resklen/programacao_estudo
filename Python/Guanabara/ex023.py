"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela
cada um dos dígitos separados
"""
# numero = input('Digite um número entre 0 e 9999: ')
# uni = numero[3]
# dez = numero[2]
# cen = numero[1]
# mil = numero[0]
# print('Analisando o número {}',format(numero))
# print('Unidade: {}'.format(uni))
# print('Dezena: {}'.format(dez))
# print('Centena: {}'.format(cen))
# print('Milhar: {}'.format(mil))
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('milhar: {}'.format(m))
