"""
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. Pergunte o valor da casa, o
salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou
então o empréstimo será negado.
"""
casa = float(input('Digite o valor da cada em R$: '))
salario = float(input('Digite seu salário: '))
ano = int(input('Digite em quantos anos você vai pagar: '))

meses = ano * 12
prestacao = casa / meses
condicao = prestacao <= 0.30 * salario

if condicao:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado.')

print('Para pagar uma casa de R${:.2f} em {} anos, '.format(casa, ano), end='')
print('a prestação será de R${:.2f}'.format(prestacao))
