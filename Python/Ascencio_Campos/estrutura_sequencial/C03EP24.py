"""
Faça um programa que receba a quantidade de dinheiro em reais que uma pessoa
que vai viajar possui. Ela vai passar por vários países e precisa converter
seu dinheiro em dólares, marco alemão e libra esterlina.

"""
valor_real = float(input('Insira a quantidade de dinheiro em real: R$ '))

valor_dolar = valor_real / 5.14
valor_alemao = valor_real / 3.06
valor_libra = valor_real / 6.81

print(f'R$ {valor_real:.2f} equivale a US$ {valor_dolar:.2f};')
print(f'R$ {valor_real:.2f} equivale a {valor_alemao:.2f} marcos alemão;')
print(f'R$ {valor_real:.2f} equivale a {valor_libra:.2f} libras esterlinas.')
