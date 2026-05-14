"""
Faça um programa que receba:
- O código de um produto comprado, supondo que a digitação do código do produto
seja sempre válida, isto é, um número inteiro entre 1 e 10.
- O peso do produto em quilos.
- O código do país de origem, supondo que a digitação do código seja sempre
válida, isto é, um número inteiro entre 1 e 3:

CÓDIGO DO PAÍS DE ORIGEM            IMPOSTO
        1                               0%
        2                               15%
        3                               25%

CÓDIGO DO PRODUTO                   PREÇO POR GRAMA
    1 a 4                               10
    5 a 7                               25
    8 a 10                              35

Calcule e mostre:
- o peso do produto convertido em gramas;
- o preço total do produto comprado;
- o valor do imposto, sabendo que ele é cobrado sobre o preço total do
produto comprado e depende do país de origem;
- o valor total, preço total do produto mais imposto.
"""

codigo_produto = int(input('Digite o código do produto: '))
peso_kg = float(input('Insira o peso do produto em kg: '))
codigo_pais = int(input('Insira o código do país: '))

peso_g = peso_kg * 1000

if codigo_pais == 1:
    if 1 <= codigo_produto <= 4:
        preco = peso_g * 10
        imposto = 0
        valor_total = preco + imposto

    elif 5 <= codigo_produto <= 7:
        preco = peso_g * 25
        imposto = 0.15
        valor_total = preco + imposto

    elif 8 <= codigo_produto <= 10:
        preco = peso_g * 35
        imposto = 0.25
        valor_total = preco + imposto

elif codigo_pais == 2:
    if 1 <= codigo_produto <= 4:
        preco = peso_g * 10
        imposto = 0
        valor_total = preco + imposto

    elif 5 <= codigo_produto <= 7:
        preco = peso_g * 25
        imposto = 0.15
        valor_total = preco + imposto

    elif 8 <= codigo_produto <= 10:
        preco = peso_g * 35
        imposto = 0.25
        valor_total = preco + imposto

elif codigo_pais == 3:
    if 1 <= codigo_produto <= 4:
        preco = peso_g * 10
        imposto = 0
        valor_total = preco + imposto

    elif 5 <= codigo_produto <= 7:
        preco = peso_g * 25
        imposto = 0.15
        valor_total = preco + imposto

    elif 8 <= codigo_produto <= 10:
        preco = peso_g * 35
        imposto = 0.25
        valor_total = preco + imposto

print(f'O peso do produto, em gramas, é de {peso_g:.2f} g.')
print(f'O preço total do produto comprado é R$ {preco:.2f}.')
print(f'O valor do imposto é de R$ {imposto:.2f}.')
print(f'O valor total do produto é de R$ {valor_total:.2f}.')
