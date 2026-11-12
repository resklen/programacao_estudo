distancia = float(input('Digite a distância percorrida em km: '))
dias = int(input('Por quantos dias o carro foi alugado? '))

preco = 60 * dias + 0.15 * distancia

print('Você deverá pagar R${:.2f}'.format(preco))
