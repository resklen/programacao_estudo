"""
Faça um programa que receba dois número e mostre o maior.

"""
primeiro_numero = float(input('Insira o primeiro número: '))
segundo_numero = float(input('Insira o segundo número: '))

if primeiro_numero > segundo_numero:
    print(f'O {primeiro_numero} é maior do que o {segundo_numero}')
elif primeiro_numero < segundo_numero:
    print(f'O {segundo_numero} é maior do que o {primeiro_numero}')
else:
    print('Os números são iguais')
