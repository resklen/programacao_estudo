"""
Faça um programa que receba o valor de um depósito e o valor
da taxa de juros, calcule e mostre o valor do rendimento e o
valor total depois do rendimento.

"""
valor_deposito = float(input('Insira o valor do depósito: R$ '))
taxa_juros = float(input('Insira a taxa de juros (%): '))

valor_rendimento = valor_deposito * taxa_juros / 100
valor_total = valor_deposito + valor_rendimento

print(f'O rendimento foi de R$ {valor_rendimento:.2f}')
print(f'O valor total é de R$ {valor_total:.2f}')
