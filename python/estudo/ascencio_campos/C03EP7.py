"""
Faça um programa que receba o peso de uma pessoa, calcule e mostre:

a) o novo peso, se a pessoa engordar 15% sobre o peso digitado;
b) o novo peso, se a pessoa emagrecer 20% do peso digitado.

"""
peso = float(input('Insira seu peso em kg: '))

peso_novo_engordou = peso + 0.15 * peso
peso_novo_emagreceu = peso - 0.2 * peso

print(f'Se você engordar 15%, seu novo peso será de {peso_novo_engordou:.2f}kg')
print(f'Se você emagrecer 20%, seu novo peso será de {peso_novo_emagreceu:.2f}kg')
