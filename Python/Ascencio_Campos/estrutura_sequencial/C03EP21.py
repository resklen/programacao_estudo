"""
Faça um programa que receba o número de horas trabalhadas, o valor do salário
mínimo e o número de horas extras trabalhadas, calcule e mostre o salário a
receber, de acordo com as regras a seguir:

a) a hora trabalhada vale 1/8 do salário mínimo;
b) a hora extra vale 1/4 do salário mínimo;
c) o salário bruto equivale ao número de horas trabalhadas multiplicado 
pelo valor da hora trabalhada;
d) a quantia a receber pelas horas extras equivale ao número de horas extras
trabalhadas multiplicado pelo valor da hora extra;
e) o salário a receber equivale ao salário bruto mais a quantia a receber pelas
horas extras.

"""
horas_trabalhadas = int(input('Insira o número de horas trabalhadas: '))
salario_minimo = float(input('Insira o valor do salário mínimo: R$ '))
horas_extras = int(input('Insira o número de horas extras trabalhadas: '))

hora_trabalhada = (1/8) * salario_minimo
hora_extra = (1/4) * salario_minimo
salario_bruto = horas_trabalhadas * hora_trabalhada
salario_extra = horas_extras * hora_extra
salario_receber = salario_bruto + salario_extra

print(f'O salário a receber é de: R$ {salario_receber:.2f}')
