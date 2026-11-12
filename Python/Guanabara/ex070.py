"""
Crie um programa que leia o nome e o preço de vários
produtos. O programa deverá perguntar se o usuário vai
continuar ou não. No final, mostre:

A) Qual é o total gasto na compra.

B) Quantos produtos custam mais de R$1000,00

C) Qual é o nome do produto mais barato

"""
# total = 0
# maisdemil = 0
# barato = 0
# maisbarato = ' '
# while True:
#     nome = str(input('Digite o nome do produto: '))
#     preco = float(input('Digite o valor do produto: R$'))
    
#     if barato == 0:
#         barato = preco
#         maisbarato = nome
#     else:
#         if preco < barato:
#             barato = preco
#             maisbarato = nome

#     if preco >= 1000:
#         maisdemil += 1
    
#     total += preco

#     continuar = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]
#     if continuar == 'N':
#         break

# print(f'O total gasto na compra foi R${total:.2f}')
# print(f'{maisdemil} produtos custam mais de R$1000,00')
# print(f'O produto mais barato foi {maisbarato} que custa R${barato:.2f}.')

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato custa R${menor:.2f}')