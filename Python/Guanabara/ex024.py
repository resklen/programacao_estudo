"""
Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com o nome "SANTO".
"""
# cidade = input('Digite o nome da cidade: ')

# lista = cidade.split()
# primeiro_nome = lista[0]

# if lista[0] == 'Santo' or lista[0] == 'São':
#     print('Sua cidade começa com o nome "Santo"')
# else:
#     print('Sua cidade não começa com o nome "Santo"')

cid = str(input('Em qual cidade você nasceu? ')).strip() # strip elimina os espaços
print(cid[:5].upper() == 'SANTO') # pega qualquer coisa digitada pelo usuário e transforma em maiúscula
