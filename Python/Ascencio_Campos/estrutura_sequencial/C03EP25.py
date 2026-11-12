"""
Faça um programa que receba uma hora (uma variável para hora e outra para minutos), calcule e mostre:

a) a hora digitada convertida em minutos;
b) o total dos minutos, ou seja, os minutos digitados mais a conversão anterior
c) o total dos minutos convertidos em segundos.

"""
horas = int(input('Insira a hora: '))
minutos = int(input('Insira os minutos: '))

hora_em_minuto = horas * 60
minutos_total = minutos + hora_em_minuto
segundos_total = minutos_total * 60

print(f'{horas} horas equivalem a {hora_em_minuto} minutos;')
print(f'O total de minutos é {minutos_total} e o total de segundos é {segundos_total}')
