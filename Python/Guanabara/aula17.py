# num = [2, 5, 9, 1]

# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 2)
# num.remove(2)
# print(num)
# print(f'Essa lista tem {len(num)} elementos')

# valores = []

# valores.append(5)
# valores.append(9)
# valores.append(4)

# for v in valores:
#     print(f'{v}...', end='')

# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}. ')
# print('Cheguei ao final da lista. ')

# valores = list()

# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))

# for c, v in enumerate(valores):
#     print(f'Eu encontrei o valor {v} na posição {c}')

a = [2, 3, 4, 7]
b = a[:]        # Se colocar só b = a o python cria uma ligação. Desse jeito ele só copia os valores
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
