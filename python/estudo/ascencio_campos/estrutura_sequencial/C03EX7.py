"""
Faça um programa que receba o salário base de um funcionário, 
calcule e mostre seu salário a receber, sabendo-se que o funcionário
tem gratificação de R$ 50 e paga imposto de 10% sobre o salário base.

"""
gratificacao = 50
salario_base = float(input('Insira seu salário: R$ '))

imposto = 0.10 * salario_base
salario_a_receber = salario_base + gratificacao - imposto

print(f'Gratificação: R$ {gratificacao:.2f}')
print(f'Imposto: R$ {imposto:.2f}')
print(f'Salário a receber: R$ {salario_a_receber:.2f}')
