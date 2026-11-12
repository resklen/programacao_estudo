"""
Faça um programa que receba o salário de um funcionário e o
percentual de aumento, calcule e mostre o valor do aumento
e o novo salário.

"""
salario = float(input('Informe seu salário: '))
aumento_perc = float(input('Informe o percentual de aumento: '))

aumento = (aumento_perc / 100) * salario
novo_salario = salario + aumento

print(f'Valor do aumento: R${aumento:.2f}')
print(f'Novo salário: R${novo_salario:.2f}')
