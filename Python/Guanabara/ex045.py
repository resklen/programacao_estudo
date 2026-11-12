# from random import randint
# from time import sleep
# print('''Suas opções:
# [ 0 ] PEDRA
# [ 1 ] PAPEL
# [ 2 ] TESOURA''')


# jogada = int(input('Qual é a sua jogada?\n'))
# computador = randint(0, 2)
# sleep(1)
# print('JO')
# sleep(1)
# print('KEN')
# sleep(1)
# print('PO!')
# if jogada == 0:
#     print('-=' * 13)
#     print('O jogador jogou PEDRA')
#     if computador == 0:
#         print('O computador jogou PEDRA')
#         print('-=' * 13)
#         print('JOGO EMPATADO!')
#     elif computador == 1:
#         print('O computador jogou PAPEL')
#         print('-=' * 13)
#         print('O COMPUTADOR VENCEU!')
#     elif computador == 2:
#         print('O computador jogou TESOURA')
#         print('-=' * 13)
#         print('VOCÊ VENCEU!')

# elif jogada == 1:
#     print('-=' * 13)
#     print('O jogador jogou PAPEL')
#     if computador == 0:
#         print('O computador jogou PEDRA')
#         print('-=' * 13)
#         print('VOCÊ VENCEU!')
#     elif computador == 1:
#         print('O computador jogou PAPEL')
#         print('-=' * 13)
#         print('JOGO EMPATADO!')
#     elif computador == 2:
#         print('O computador jogou TESOURA')
#         print('-=' * 13)
#         print('O COMPUTADOR VENCEU!')
# elif jogada == 2:
#     print('-=' * 13)
#     print('O jogador jogou TESOURA')
#     if computador == 0:
#         print('O computador jogou PEDRA')
#         print('-=' * 13)
#         print('O COMPUTADOR VENCEU!')
#     elif computador == 1:
#         print('O computador jogou PAPEL')
#         print('-=' * 13)
#         print('VOCÊ VENCEU!')
#     elif computador == 2:
#         print('O computador jogou TESOURA')
#         print('-=' * 13)
#         print('JOGO EMPATADO!')
# else:
#     print('Opção inválida.')

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')    
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Joagada inválida.')
elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')    
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida.')
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')    
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida.')
