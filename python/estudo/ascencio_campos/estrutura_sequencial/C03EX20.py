"""
Faça um programa que receba a medida do ângulo (em graus) formado por uma
escada apoiada no chão e encostada na parede e a altura da parede onde está
a ponta da escada. Calcule e mostre a medida dessa escada.

"""
import math 

angulo_grau = float(input('Insira o valor do ângulo (em graus) formado entre a escada e o chão: '))
altura_parede = float(input('Insira a altura da parede (em metros) onde a escada está apoiada: '))

angulo_rad = math.radians(angulo_grau)
comprimento_escada = altura_parede / math.sin(angulo_rad)

print(f'O comprimento da escada é de {comprimento_escada:.2f} m.')
