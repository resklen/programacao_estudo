"""
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
será adicionado. No final, serão exibidos todos os valores únicos 
digitados, em ordem crescente.

"""
valores = list()
opcao = 0


while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:         
        valores.append(valor)
    else:
        print('Esse valor já foi inserido. ')

    opcao = str(input('Quer continuar: [S/N] ')).strip().upper()
    if opcao in 'N':
        break

valores.sort()
print(f'Os valores digitados pelo usuário foram: {valores}')
