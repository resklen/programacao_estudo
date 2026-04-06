"""
Faça um programa que receba o custo de um espetáculo teatral
e o preço do convite desse espetáculo. Esse programa deverá calcular
e mostrar a quantidade de convites que devem ser vendidos para que,
pelo menos, o custo do espetáculo seja alcançado.

"""
from math import ceil
custo_espetaculo = float(input('Insira o custo do espetáculo teatral: R$ '))
preco_convite = float(input('Insira o preço do convite desse espetáculo: R$ '))

quantidade_convites = ceil(custo_espetaculo / preco_convite)

print(f'Para que pelo menos o custo do espetáculo seja alcançado,\
deverá ser vendido {quantidade_convites} convites. ')
