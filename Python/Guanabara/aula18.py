# teste = list()

# teste.append('Vinicius')
# teste.append(30)

# print(teste)

# galera = list()

# galera.append(teste[:])
# print(galera)

# teste[0] = 'João'
# teste[1] = 27

# galera.append(teste[:])
# print(galera)

# galera = [['João', 27], ['Maria', 45], ['Vinicius', 30], ['Ana', 33]]

# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade. ')

galera = list()
dado = list()
total_maior = total_menor = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade. ')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade. ')
        total_menor +=1

print(f'Temos {total_maior} maiores de idade e {total_menor} menores de idade')


