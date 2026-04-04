"""
Faça um programa que receba o peso de uma pessoa em quilos, calcule e mostre
esse pesso em gramas.

"""
peso_kg = float(input('Insira seu peso em kg: '))

peso_g = peso_kg * 1000

print(f'{peso_kg} kg equivale a {peso_g:.2f} g ')
