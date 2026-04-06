"""
Faça um programa que receba o salário de um funcionário, calcule
e mostre o novo salário, sabendo-se que este sofreu um aumento de
25%

"""
salario = float(input('Informe seu salário: R$'))

novo_salario = salario + 0.25 * salario

print(f'Seu novo salário, com 25% de aumento, é de R${novo_salario:.2f}')
