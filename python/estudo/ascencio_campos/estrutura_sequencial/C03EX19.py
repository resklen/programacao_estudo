"""
Cada degrau de uma escada tem X de altura. Faça um programa que receba essa
altura e a altura que o usuário deseja alcançar subindo a escada, calcule e 
mostre quantos degraus ele deverá subir para atingir seu objetivo, sem se 
preocupar com a altura do usuário. Todas as medidas fornecidas devem estar
em metros.

"""
from math import ceil

altura_degrau = float(input('Insira a altura (m) do degrau: '))
altura_desejada = float(input('Insira a altura (m) que você deseja alcançar subindo a escada: '))

quant_degraus = ceil(altura_desejada / altura_degrau)

print(f'Você deverá subir {quant_degraus} degraus')
