"""
Escreva um programa em Python que leia um número inteiro
qualquer e peça para o usuário escolher qual será a base
de conversão: 1 para binário, 2 para octal e 3 para hexadecimal
"""
numero = int(input('Digite um número inteiro qualquer: '))

base = int(input('''Qual será a base de conversão?\n
[ 1 ] - BINÁRIO\n
[ 2 ] - OCTAL\n
[ 3 ] - HEXADECIMAL\n\n'''))
if base == 1:
    print('Você escolheu BINÁRIO.')
    print('{} convertido para binário é {}'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('Você escolheu OCTAL.')
    print('{} convertido para octal é {}'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('Você escolheu HEXADECIMAL.')
    print('{} convertido em hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Você digitou um número inválido.')
