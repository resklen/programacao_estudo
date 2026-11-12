"""
Faça um programa que calcule e mostre a área de um círculo.

"""
from math import pi

raio = float(input('Insira o raio do círculo em m: '))

area = pi * raio ** 2

print(f'A área de um círculo de raio {raio} m é de {area:.2f} m².')
