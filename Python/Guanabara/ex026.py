"""
Faça um programa que leia uma frase pelo teclado e mostre
quantas vezes aparece a letra "A", em qual posição ela aparece
a primeira vez e em qual posição ela aparece a última vez.
"""
frase = input('Digite uma frase: ')

frase_maiusc = frase.upper().strip()
tem_a = 'A' in frase_maiusc
cont = frase_maiusc.count('A')
pos_i = frase_maiusc.find('A') + 1
pos_f = frase_maiusc.rfind('A') + 1

print('Tem "A" na frase? {}'.format(tem_a))
print('A letra "A" aparece {} vezes.'.format(cont))
print('A letra "A" aparece a primeira vez na posição {}'.format(pos_i))
print('A letra "A" aparece pela última vez na posição {}'.format(pos_f))
