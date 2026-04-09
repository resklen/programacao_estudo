"""
Faça um programa que mostre a data e a hora do sistema nos seguintes formatos:
DD/MM/AAAA - mês por extenso e hora:minuto.

"""
from datetime import datetime

agora = datetime.now()

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

data_formatada = agora.strftime('%d/%m/%Y')
hora_formatada = agora.strftime('%H:%M')
mes_extenso = meses[agora.month - 1]


print(f'{data_formatada} - {mes_extenso} - {hora_formatada}')
