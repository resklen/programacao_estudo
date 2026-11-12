"""
Faça um programa que receba o salário inicial de um funcionário, 
calcule e mostre o novo salário acrescido de bonificação e auxílio
escola.


    SALÁRIO                 BONIFICAÇÃO
Até R$500,00                5% do salário
Entre R$500,00 e R$1200,00  12% do salário
Acima de R$1200,00          Sem bonificação

    SALÁRIO                 AUXÍLIO ESCOLA
Até R$600,00                R$150,00
Acima de R$600,00           R$100,00
"""

salario_inicial = float(input('Insira seu salário: R$ '))

if salario_inicial <= 500:
    bonificacao = 0.05 * salario_inicial
    
elif salario_inicial <= 1200:
    bonificacao = 0.12 * salario_inicial

else:
    bonificacao = 0

if salario_inicial <= 600:
    auxilio = 150

else:
    auxilio = 100

salario_final = salario_inicial + bonificacao + auxilio

print(f'Seu salário final será de R$ {salario_final:.2f}')
