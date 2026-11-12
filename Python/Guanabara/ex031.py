"""
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até
200 km e R$0,45 para viagens mais longas
"""
# distancia = float(input('Digite a distância da viagem em km: '))

# preco1 = distancia * 0.5
# preco2 = distancia * 0.45

# if distancia > 200:
#     print('Você deverá pagar R${:.2f}'.format(preco2))
# else:
#     print('Você deverá pagar R${:.2f}'.format(preco1))

distancia = float(input('Digite a distância da viagem em km: '))

if distancia > 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.5

print('O preço da viagem de {:.0f} km é R${:.2f}'.format(distancia, preco))
