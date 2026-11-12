"""
Faça um programa que receba três notas e seus respectivos pesos,
calcule e mostre a média ponderada.

"""
nota1 = float(input('Digite a primeira nota: '))
peso1 = int(input('Insira o peso da primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
peso2 = int(input('Insira o peso da segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
peso3 = int(input('Insira o peso da terceira nota: '))

soma_notas = nota1 * peso1 + nota2 * peso2 + nota3 * peso3
soma_pesos = peso1 + peso2 + peso3
media_ponderada = soma_notas / soma_pesos

print(f'A média ponderada das três notas inseridas é {media_ponderada:.1f}')
