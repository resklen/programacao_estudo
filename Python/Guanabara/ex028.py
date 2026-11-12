"""
Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador. O programa deverá escrever na tela se o
usuário venceu ou perdeu.
"""
# from random import randint

# num_usuario = int(input('Tente adivinhar um número entre 0 e 5. '))

# num_pensado = randint(0, 5)
# print(num_pensado)
# if num_usuario == num_pensado:
#     print('Você venceu!')
# else:
#     print('Você perdeu!')

from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "pensar"
print('-=-' * 13)
print('Vou pensar em um número entre 0 e 5.')
print('-=-' * 13)
jogador = int(input('Em qual número pensei?\n')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Você venceu!')
else:
    print('Eu pensei no número {}, e não no {}. Você perdeu!'.format(computador, jogador))
