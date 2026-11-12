"""
Faça um programa que receba duas notas, calcule e mostre a média ponderada
dessas notas, considerando peso 2 para a primeira e peso 3 para segunda.

"""
primeira_nota = float(input('Insira a primeira nota: '))
segunda_nota = float(input('Insira a segunda nota: '))

media_ponderada = ((primeira_nota * 2) + (segunda_nota * 3)) / (2 + 3)

print(f'A média ponderada de {primeira_nota} com peso 2 e a {segunda_nota} com peso 3\
é igual a {media_ponderada:.2f}')
