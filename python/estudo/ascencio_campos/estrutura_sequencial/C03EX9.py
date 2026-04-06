"""
Faça um programa que calcule e mostre a área de um triângulo.

"""
base = float(input('Insira a base do triângulo em cm: '))
altura = float(input('Insira a altura do triângulo em cm: '))

area = (base * altura) / 2

print(f'O triângulo de base {base} cm e altura {altura} cm tem {area:.2f} cm² de área.')
