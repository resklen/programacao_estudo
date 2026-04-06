"""
Faça um programa que receba o valor do salário mínimo e o valor do salário
de um funcionário, calcule e mostre a quantidade de salários mínimos que 
esse funcionário ganha.

"""
salario_minimo = float(input('Insira o valor do salário mínimo: R$ '))
salario_funcionario = float(input('Insira o valor do salário do funcionário: R$'))

quantidade_minimos = salario_funcionario / salario_minimo

print(f'Você recebe o equivalente a {quantidade_minimos:.2f} salários mínimos')
