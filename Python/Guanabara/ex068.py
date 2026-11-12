"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando
o total de vitórias consecutivas qe ele conquistou no final do
jogo.

"""
# from random import randint

# while True:

#     escolha = str(input('Par ou ímpar? [P/I] ')).upper()
    
#     if escolha not in 'PpIi':
#         break
    
#     jogador = int(input('Seu número: '))
#     computador = randint(0, 10)   
   
#     total = computador + jogador
#     resultado_par = total % 2 == 0
#     resultado_impar = total % 2 != 0

#     if resultado_par:
#         if escolha in 'Pp':
#             print(f'Você jogou {jogador} e o computador {computador}')
#             print(f'O total {total} é par\nVocê venceu!')
#         elif escolha in 'Ii':
#             print(f'Você jogou {jogador} e o computador {computador}')
#             print(f'O total deu {total} um número par\nVocê perdeu!')


#     if resultado_impar:
#         if escolha in 'Pp':
#             print(f'Você jogou {jogador} e o computador {computador}')
#             print(f'O total é {total}, um número ímpar\nVocê perdeu!')
#         elif escolha in 'Ii':
#             print(f'Você jogou {jogador} e o computador {computador}')
#             print(f'O total é {total}, um número ímpar.\nVocê venceu!')
    
#     if escolha not in 'PpIi':
#         break

from random import randint

v = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.', end='')
    print('Deu par' if total % 2 == 0 else 'Deu ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            
            v += 1
        else:
            print('Você perdeu!')
            break

    if tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente...')
print(f'Game over, você venceu {v} vezes.')
