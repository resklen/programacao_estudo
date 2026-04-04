"""
Faça um programa que receba o preço de um produto, calcule e mostre o novo
preço, sabendo-se que este sofreu um desconto de 10%.

"""

preco_produto = float(input('Insira o preço do produto: R$ '))

novo_preco = preco_produto - 0.1 * preco_produto

print(f'O preço do produto, com 10% de desconto, é de R$ {novo_preco:.2f}')
