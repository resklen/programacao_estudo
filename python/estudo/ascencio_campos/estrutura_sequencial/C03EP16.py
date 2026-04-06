"""
Faça um programa que receba o valor dos catetos de um triângulo, calcule
e mostre o valor da hipotenusa

"""
from math import sqrt
cateto_oposto = float(input('Insira o valor do cateto oposto: '))
cateto_adjacente = float(input('Insira o valor do cateto adjacente: '))

hipotenusa = sqrt(pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))

print(f'O valor da hipotenusa é: {hipotenusa:.2f}')
