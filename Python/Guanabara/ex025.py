"""
Crie um programa que leia o nome de uma pessoa e diga se ela
tem "SILVA" no nome
"""
nome = str(input('Digite seu nome: ')).strip()

nome_maiusc = nome.upper()
tem_silva = nome_maiusc.find('SILVA') # print('Seu nome tem Silva {}).format('silva' in nome.lower()))
print('Seu nome tem Silva {}'.format('SILVA' in nome_maiusc))

if tem_silva == -1:
    print('Você não tem "Silva" no nome.')
else:
    print('Você tem "Silva" no nome.')
