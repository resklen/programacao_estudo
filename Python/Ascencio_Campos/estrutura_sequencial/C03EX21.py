"""
Uma pessoa deseja pregar um quadro em uma parede. Faça um programa para calcular
e mostrar a que distância a escada deve estar da parede. A pessoa deve fornecer 
o tamanho da escada e a altura em que deseja pregar o quadro.
Lembre-se de que o tamanho da escada deve ser maior que a altura que se deseja
alcançar.

"""
from math import sqrt

tamanho_escada = float(input('Insira o tamanho da escada (em metros): '))
altura_quadro = float(input('Insira a altura (em metros) que o quadro deverá ficar: '))

if tamanho_escada > altura_quadro:
    distancia_escada = sqrt(tamanho_escada ** 2 - altura_quadro ** 2)

    print(f'A distância em que a escada deve estar da parede é de {distancia_escada:.2f} m')
else:
    print('O comprimento da escada deve ser maior do que a altura do quadro. ')
