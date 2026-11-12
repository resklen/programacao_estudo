"""
Crie um programa que mostre na tela todos os números
pares que estão no intervalo entre 1 e 50.

"""
# Solução mais otimizada (pensada por mim)
# print('Os números pares de 1 a 50 são: ')
# for c in range(2, 51, 2):
#     print(c)
# print('FIM')

# Solução clássica
print('Os números pares de 1 a 50 são:')

for c in range(1, 51):
    if c % 2 == 0:
        print('{}'.format(c), end=' ')
print('\nFIM')
