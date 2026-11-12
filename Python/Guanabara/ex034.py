"""
Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores a 
R$1250.00, calcule um aumento de 10%. Para os inferiores ou 
iguais, o aumento é de 15%.
"""
salario = float(input('Digite o valor do seu salário: '))

inferior = salario <= 1250

if inferior:
    novo_sal = salario + 0.15 * salario
else:
    novo_sal = salario + 0.10 * salario

print('Seu salário de R${:.2f} foi para R${:.2f} com o aumento'.format(salario, novo_sal))
