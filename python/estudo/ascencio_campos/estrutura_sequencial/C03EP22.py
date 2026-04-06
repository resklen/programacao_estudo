"""
Faça um programa que receba o número de lados de um polígono convexo, calcule
e mostre o número de diagonais desse polígono.

"""
numero_lados = int(input('Insira o número de lados do polígono convexo: '))

numero_diagonais = numero_lados * (numero_lados - 3) / 2

print(f'Esse polígono possui {numero_diagonais:.0f} diagonais. ')
