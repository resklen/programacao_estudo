"""
Faça um programa que receba o valor do salário mínimo, o número de horas trabalhadas,
o número de dependentes do funcionário e a quantidade de horas extras trabalhadas.
Calcule e mostre o salário a receber do funcionário de acordo com as regras a seguir:

- O valor da hora trabalhada é igual a 1/5 do salário mínimo
- O salário do mês é igual ao número de horas trabalhadas multiplicado pelo valor
da hora trabalhada
- Para cada dependente, acrescentar R$32,00
- Para cada hora extra trabalhada, calcular o valor da hora trabalhada acrescida de 50%
- O salário bruto é igual ao salário do mês mais o valor dos dependentes mais o
valor das horas extras
- Calcular o valor do imposto de renda retido na fonte de acordo com a tabela a seguir:

    IRPF            SALÁRIO BRUTO
    Isento          Inferior a R$ 200,00
    10%             De R$200,00 até R$500,00
    20%             Superior a R$500,00

- O salário líquido é igual ao salário bruto menos IRRF
- A gratificação é de acordo com a tabela a seguir:

    SALÁRIO LÍQUIDO             GRATIFICAÇÃO
    Até R$ 350.00               R$ 100.00
    Superior a R$ 350.00        R$ 50.00

- O salário a receber do funcionário é igual ao salário líquido mais a gratificação.

"""

salario_minimo = float(input('Insira o valor do salário mínimo: R$ '))
horas_trabalhadas = float(input('Insira o número de horas trabalhadas: '))
dependentes = int(input('Insira a quantidade de dependentes que você possui: '))
horas_extras = float(input('Insira a quantidade de horas extras trabalhadas: '))

valor_hora = (1/5) * salario_minimo
salario_mes = horas_trabalhadas * valor_hora
acrescimo_dependente = 32 * dependentes
total_hora_extra = 1.5 * valor_hora * horas_extras

salario_bruto = salario_mes + acrescimo_dependente + total_hora_extra

if salario_bruto > 500:
    imposto_renda = 0.2 * salario_bruto

elif salario_bruto >= 200 and salario_bruto <= 500:
    imposto_renda = 0.1 * salario_bruto

else:
    imposto_renda = 0

salario_liquido = salario_bruto - imposto_renda

if salario_liquido > 350:
    gratificacao = 50
else:
    gratificacao = 100

salario_receber = salario_liquido + gratificacao

print(f'O seu salário será de R$ {salario_receber:.2f}.')
