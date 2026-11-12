"""
Faça um programa que calcule e mostre a área de um losango. Sabe-se que:
A = (diagonal maior * diagonal menor) / 2

"""
diagonal_maior = float(input('Insira o valor da diagonal maior do losango: '))
diagonal_menor = float(input('Insira o valor da diagonal menor do losango: '))

area = (diagonal_maior * diagonal_menor) / 2

print(f'A árena do losango é de {area:.2f}')
