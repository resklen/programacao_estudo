"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:

A) Quantos números foram digitados
B) A lista de valores ordenada de forma decrescente
C) Se o número 5 foi digitado e está ou não na lista.

"""
lista = list()

while True:
    
    valor = int(input('Digite o valor a ser inserido na lista: '))
    lista.append(valor)
    opcao = input('Deseja inserir mais algum valor? [S/N]').upper().strip()[0]
    if opcao in 'N':
        break

numeros_digitados = len(lista)
print(f'Foram digitados {numeros_digitados} valores na lista')
print(f'Os valores da lista foram: {lista}')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é: {lista}')

if 5 in lista:
    print('O cinco foi digitado e está na lista. ')
else:
    print('O cinco não está na lista. ')