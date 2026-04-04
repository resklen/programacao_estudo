"""
Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas.
Faça um programa que receba o salário fixo do funcionário e o valor de suas 
vendas, calcule e mostre a comissão e seu salário final.

"""
salario_fixo = float(input('Insira o salário fixo do funcionário: R$ '))
vendas = float(input('Insira o valor de suas vendas: R$ '))

comissao = 0.04 * vendas
salario_final = salario_fixo + comissao

print(f'A comissão foi de R$ {comissao:.2f} e o salário final é R$ {salario_final:.2f}')
