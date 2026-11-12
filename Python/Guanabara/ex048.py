"""
Faça um programa que calcule a soma entre todos os números ímpares
que são múltiplos de três e que se encontram no intervalo
de 1 até 500.
"""
soma = 0
contador = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n       # soma = soma + n
        contador += 1   # contador = contador + 1
print('A soma entre os {} números ímpares múltiplos de três ' \
'entre 1 e 500 é {}'.format(contador, soma))
print('FIM')

