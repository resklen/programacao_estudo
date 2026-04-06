"""
Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual,
calcule e mostre:
a) a idade dessa pessoa em anos;
b) a idade dessa pessoa e meses;
c) a idade dessa pessoa em dias;
d) a idade dessa pessoa em semanas.

"""
from math import ceil
from datetime import date
ano_nascimento = int(input('Insira o ano do seu nascimento: '))

idade_anos = date.today().year - ano_nascimento
idade_meses = idade_anos * 12
idade_dias = idade_meses * 30
idade_semanas = ceil(idade_dias / 7)

print(f'Sua idade, em anos, é {idade_anos}')
print(f'Sua idade, em meses, é {idade_meses}')
print(f'Sua idade, em dias, é {idade_dias}')
print(f'Sua idade, em semanas, é {idade_semanas} ')
