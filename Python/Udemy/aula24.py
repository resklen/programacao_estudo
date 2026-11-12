# in e not in

nome = 'Vinicius'

# print(nome[0])

# print('Vi' in nome)
# print('zero' in nome)
# print(10 * '-')
# print ('Vini' not in nome)
# print('zero' not in nome)

nome = input('Digite um nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')