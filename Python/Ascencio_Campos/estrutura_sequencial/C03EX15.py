"""
O custo ao consumidor de um carro novo é a soma do preço
de fábrica com o percentual de lucro do distribuidor e dos
impostos aplicados ao preço de fábrica. Faça um programa que
receba o preço de fábrica de um veículo, o percentual de lucro
do distribuidor e o percentual de impostos, calcule e mostre:

a) O valor correspondente ao lucro do distribuidor;
b) o valor correspondente aos impostos;
c) O preço final do veículo

"""
preco_fabrica = float(input('Insira o preço de fábrica do veículo: R$ '))
lucro_perc = float(input('Insira o percentual de lucro do distribuidor (%): '))
imposto_perc = float(input('Insira o percentual de impostos (%): '))

lucro_distribuidor = (preco_fabrica * lucro_perc) / 100
imposto_aplicado = (preco_fabrica * imposto_perc) / 100
preco_final = preco_fabrica + lucro_distribuidor + imposto_aplicado

print(f'O valor correspondente ao lucro do distribuidor é de R${lucro_distribuidor:.2f}')
print(f'O valor correspondente aos impostos é de R${imposto_aplicado:.2f}')
print(f'O preço final do veículo é de R${preco_final:.2f}')
