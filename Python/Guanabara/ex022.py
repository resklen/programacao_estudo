"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas;
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome
"""
nome = input('Digite seu nome completo: ')

maiscula = nome.upper()
minuscula = nome.lower()
comprimento = len(nome)
letras = comprimento - nome.count(' ')
lista = nome.split()
letras_primeiro = len(lista[0])

print('Nome em maiúsculas: {}.'.format(maiscula))
print('Nome em minúsculas: {}.'.format(minuscula))
print('Seu nome possui {} letras.'.format(letras))
print('Seu primeiro nome possui {} letras.'.format(letras_primeiro))