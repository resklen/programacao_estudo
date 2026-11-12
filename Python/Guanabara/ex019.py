# import random
# primeiro_aluno = input('Digite o nome do primeiro aluno: ')
# segundo_aluno = input('Digite o nome do segundo aluno: ')
# terceiro_aluno = input('Digite o nome do terceiro aluno: ')
# quarto_aluno = input('Digite o nome do quarto aluno: ')

# sorteado = random.randint(1, 4)
# print(sorteado)

# if sorteado == 1:
#     print(f'O aluno sorteado é: {primeiro_aluno}')
# elif sorteado == 2:
#     print(f'O aluno sorteado é: {segundo_aluno}')
# elif sorteado == 3:
#     print(f'O aluno sorteado é: {terceiro_aluno}')
# else:
#     print(f'O aluno sorteado é: {quarto_aluno}')

from random import choice
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')

lista = [n1, n2, n3, n4]
escolha = choice(lista)

print('O escolhido foi: {}'.format(escolha))