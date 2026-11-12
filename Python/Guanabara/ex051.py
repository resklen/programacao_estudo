"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.

"""
a1 = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão da PA: '))

for n in range(1, 11):
    pa = a1 + (n - 1) * razao
    print('a{} = {}'.format(n, pa), end='; ')
