"""
Faça um programa que receba a hora do início de um jogo e a hora do término (cada hora
é composta por duas variáveis inteiras: hora e minuto). Calcule e mostre a duração do
jogo (horas e minutos), sabendo que o tempo máximo de duração do jogo é de 24 horas
e que ele pode começar em um dia e terminar no dia seguinte.

"""
from math import ceil

hora_inicio = int(input('Insira as horas de início do jogo: '))
minuto_inicio = int(input('Insira os minutos do início do jogo: '))
hora_termino = int(input('Insira as horas do término do jogo: '))
minuto_termino = int(input('Insira os minutos do término do jogo: '))

if minuto_inicio > minuto_termino:
    minuto_termino = minuto_termino + 60
    hora_termino = hora_termino - 1

if hora_inicio >= hora_termino:
    hora_termino = hora_termino + 24

hora_total = hora_termino - hora_inicio
minuto_total = minuto_termino - minuto_inicio

print(f'O jogo teve duração de {hora_total} horas e {minuto_total} minutos. ')
    