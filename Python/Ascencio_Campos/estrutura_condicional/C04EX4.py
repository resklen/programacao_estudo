"""
Faça um programa que receba três números e mostre-os em ordem crescente. Suponha
que o usuário digitará três números diferentes.

"""
numero_1 = float(input('Insira o primeiro número: '))
numero_2 = float(input('Insira o segundo número: '))
numero_3 = float(input('Insira o terceiro número: '))

if numero_1 < numero_2 and numero_1 < numero_3:
    if numero_2 < numero_3:
        print(f'A ordem crescente é: {numero_1}, {numero_2} e {numero_3}')
    else:
        print(f'A ordem crescente é: {numero_1}, {numero_3} e {numero_2}')

elif numero_2 < numero_1 and numero_2 < numero_3:
    if numero_1 < numero_3:
        print(f'A ordem crescente é: {numero_2}, {numero_1} e {numero_3}')
    else:
        print(f'A ordem crescente é: {numero_2}, {numero_3} e {numero_1}')

elif numero_3 < numero_1 and numero_3 < numero_2:
    if numero_1 < numero_2:
        print(f'A ordem crescente é: {numero_3}, {numero_1} e {numero_2}')
    else:
        print(f'A ordem crescente é: {numero_3}, {numero_2} e {numero_1}')
