"""
Faça um programa que receba dois números maiores que zero,
calcule e mostre um elevado ao outro.

"""
primeiro_numero = float(input('Insira o primeiro número: '))
segundo_numero = float(input('Insira o segundo número: '))

if primeiro_numero > 0 and segundo_numero > 0:

    potencia = primeiro_numero ** segundo_numero

    print(f'{primeiro_numero:.2f} elevado a {segundo_numero:.2f} é igual a {potencia:.2f}')
else:
    print('Os números devem ser positivos.')
    