"""
Faça um programa que calcule e mostre a área de um trapézio.

"""

base_maior = float(input('Insira do valor da base maior: '))
base_menor = float(input('Insira o valor da base menor: '))
altura = float(input('Insira o valor da altura: '))

area = ((base_maior + base_menor) * altura) / 2

print(f'A área do trapézio é de {area:.2f}')
