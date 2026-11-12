"""
Faça um programa que receba uma hora formada por hora e minutos 
(um número real), calcule e mostre a hora digitada apenas em
minutos. Lembre-se de que:

- para quatro e meia, deve-se digitar 4.30;
- os minutos vão de 0 a 59.

"""
from math import modf

horario = float(input('Digite o horário formado por hora e minutos: '))

minutos, hora = modf(horario)

hora_em_minutos = hora * 60

horario_em_minutos = hora_em_minutos + 100 * minutos

print(f'{horario:} equivale a {horario_em_minutos:.0f} minutos. ')
