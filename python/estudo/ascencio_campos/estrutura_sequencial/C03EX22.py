"""
Sabe-se que um quilowatt de energia custa um quinto do salário mínimo.
Faça um programa que receba o valor do salário mínimo e a quantidade
de quilowatts consumida por uma residência. Calcule e mostre:

A) O valor de cada quilowatt
B) O valor a ser pago por essa residência
C) O valor a ser pago com desconto de 15%

"""

salario_minimo = float(input('Digite o valor do salário mínimo: R$ '))
quilowatt_consumido = float(input('Insira a quantidade de quilowatts consumida: '))

valor_quilowatt = salario_minimo / 5
valor_pagar = quilowatt_consumido * valor_quilowatt
valor_desconto = valor_pagar - 0.15 * valor_pagar

print(f'O valor de cada kW é de R$ {valor_quilowatt:.2f}')
print(f'O valor a ser pago pela residência é de R$ {valor_pagar:.2f}')
print(f'O valor a ser pago, com desconto de 15%, é de R$ {valor_desconto:.2f}')
