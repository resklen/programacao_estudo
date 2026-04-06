"""
Faça um programa que receba a medida do ângulo formado por uma escada apoiada
no chão e a distância em que a escada está da parede, calcule e mostre a 
medida da escada para que se possa alcançar sua ponta.

"""
from math import radians, cos
angulo = float(input('Insira o ângulo da escada: '))
distancia = float(input('Insira a distância entre a escada e a parede: '))

angulo_rad = radians(angulo)

escada = distancia / cos(angulo_rad)

print(f'Para que se possa alcançar a ponta, a escada deve ter {escada:.2f} metros.')
