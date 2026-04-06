"""
Faça um programa que receba o número de horas trabalhadas e o valor
do salário mínimo, calcule e mostre o salário a receber, seguindo
estas regras:

a) a hora trabalhada vale a metade do salário mínimo;
b) o salário bruto equivale ao número de horas trabalhadas multiplicado
pelo valor da hora trabalhada;
c) o imposto equivale a 3% do salário bruto;
d) o salario a receber equivale ao salário bruto menos o imposto.

"""
numero_horas_trabalhadas = float(input('Digite o número de horas trabalhadas: '))
salario_minimo = float(input('Digite o valor do salário mínimo: R$'))

valor_hora_trabalhada = salario_minimo / 2
salario_bruto = numero_horas_trabalhadas * valor_hora_trabalhada
imposto = 0.03 * salario_bruto
salario_a_receber = salario_bruto - imposto

print(f'O valor da hora trabalhada foi de R${valor_hora_trabalhada:.2f}')
print(f'O salário bruto foi de R${salario_bruto:.2f}')
print(f'O imposto aplicado foi de R${imposto:.2f}')
print(f'O salário a receber é de R${salario_a_receber:.2f}')
