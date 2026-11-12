"""
Faça um programa que receba a medida de dois ângulos de um triângulo,
calcule e mostre a medida do terceiro ângulo. Sabe-se que a soma dos
ângulos de um triângulo é 180°.

"""
primeiro_angulo = float(input('Insira o valor do primeiro ângulo: '))
segundo_angulo = float(input('Insira o valor do segundo ângulo: '))

terceiro_angulo = 180 - primeiro_angulo - segundo_angulo

print(f'O terceiro ângulo mede: {terceiro_angulo:.1f}°')
