"""
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas;
B) Uma listagem com as pessoas mais pesadas;
C) Uma listagem com as pessoas mais leves.

"""

lista_pessoas = list()
dado = list()
mais_pesadas = list()
mais_leves = list()

while True:

    dado.append(input('Nome: '))
    dado.append(int(input('Peso: ')))
    lista_pessoas.append(dado[:])
    dado.clear()

    opcao = input('Deseja continuar? [S/N]').upper().strip()[0]
    if opcao in 'N':
        break

print(lista_pessoas)

