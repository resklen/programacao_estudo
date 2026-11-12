"""
Refaça o exercício 51 lendo o primeiro termo e a razão de
uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while.

"""

# a1 = int(input('Digite o primeiro termo na PA'))
# r = float(input('Digite a razão da PA'))
# n = 1
# while n in range(1, 11):

#     pa = a1 + (n - 1) * r
#     print('a{} = {}'.format(n, pa))
#     n += 1

print('-=' * 7)
print('Gerador de PA')
print('-=' * 7)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

termo = primeiro
cont = 1

while cont <= 10:

    print('{} → '.format(termo), end=' ')
    termo += razão
    cont += 1

print('FIM')
