"""
Escreva um programa que leia um número N inteiro qualquer e mostre na
tela os N primeiros elementos de uma sequência de Fibonacci. Exemplo:

0 - 1 - 1 - 2 - 3 - 5 - 8

"""
n = int(input('Digite a quantidade de termos da sequência de Fibonacci: '))

primeiro = 0
segundo = 1
cont = 3

print('{} → {} → '.format(primeiro, segundo), end='')

while cont <= n:
    terceiro = segundo + primeiro
    
    print('{} → '.format(terceiro), end='')
    cont += 1
    primeiro = segundo
    segundo = terceiro

print('FIM')

