"""
Faça um programa que receba o raio, calcule e mostre:
a) o comprimento de uma esfera
b) a area de uma esfera
c) o volume de uma esfera

"""
from math import pi

raio = float(input('Insira o raio da esfera (cm): '))

comprimento = 2 * pi * raio
area = pi * pow(raio, 2)
volume = (3/4) * pi * pow(raio, 3)

print(f'O comprimento da esfera é de {comprimento:.2f} cm.')
print(f'A área da esfera é de {area:.2f} cm²')
print(f'O volume da esfera é de {volume:.2f} cm³')
