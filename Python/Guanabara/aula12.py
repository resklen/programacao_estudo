nome = str(input('Digite seu nome: '))

if nome == 'Vinicius':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é popular!')
elif nome in 'Ana Cláudia Juliana Jéssica':
    print('Belo nome feminino!')
else: # else pode ser retirado
    print('Seu nome é bem normal.')

print('É um prazer te conhecer, {}!'.format(nome))
