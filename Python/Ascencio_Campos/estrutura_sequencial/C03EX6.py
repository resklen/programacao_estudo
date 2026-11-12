"""
Faça um programa que receba o salário base de um funcionário,
calcule e mostre o salário a receber, sabendo-se que o funcionário
tem gratificação de 5% sobre o salário base e paga imposto de 7%
também sobre o salário base.

"""
salario_base = float(input('Insira seu salário: R$'))

gratificacao = 0.05 * salario_base
imposto = 0.07 * salario_base
salario_novo = salario_base + gratificacao - imposto

print(f'Gratificação: R${gratificacao:.2f}')
print(f'Imposto: R${imposto:.2f}')
print(f'Salário a receber de R${salario_novo:.2f}')
