"""
Faça um programa que receba um número positivo e maior que zero,
calcule e mostre:

a) o número digitado ao quadrado
b) o número digitado ao cubo
c) a raiz quadrada do número digitado
d) a raiz cubica do número digitado

"""
numero = float(input('Insira um número positivo e maior do que zero: '))

if numero > 0:
    numero_ao_quadrado = numero ** 2
    numero_ao_cubo = numero ** 3
    raiz_quadrada = numero ** (1/2)
    raiz_cubica = numero ** (1/3)

    print(f'{numero} ao quadrado: {numero_ao_quadrado}')
    print(f'{numero} ao cubo: {numero_ao_cubo}')
    print(f'Raiz quadrada do {numero}: {raiz_quadrada:.2f}')
    print(f'Raiz cúbica do {numero}: {raiz_cubica:.2f}')
else:
    print(f'O número deve ser maior do que zero.')
