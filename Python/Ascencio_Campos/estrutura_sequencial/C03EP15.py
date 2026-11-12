"""
João recebeu seu salário e precisa pagar duas contas atrasadas. Em razão do atraso,
ele deverá pagar multa de 2% sobre cada conta. Faça um programa que calcule e mostre
quanto restará do salário de João.

"""
salario_inicio = float(input('Insira o salário desse mês: R$ '))
conta_um = float(input('Insira o valor da primeira conta: R$ '))
conta_dois = float(input('Insira o valor da segunda conta: R$ '))

multa_um = 0.02 * conta_um
multa_dois = 0.02 * conta_dois

salario_restante = salario_inicio - (conta_um + multa_um) - (conta_dois + multa_dois)

print(f'Ao pagar as contas, restará R${salario_restante:.2f} do seu salário')
