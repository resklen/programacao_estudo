"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, respectivamente. Ao final, mostre
o conteúdo das três listas geradas.

"""
lista_usuario = []
lista_par = []
lista_impar = []

while True:
    valor = int(input('Digite o valor a ser inserido na lista: '))
    lista_usuario.append(valor)
    opcao = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if opcao in 'N':
        break
    
for cont in lista_usuario:
    if cont % 2 == 0:
        lista_par.append(cont)
    else:
        lista_impar.append(cont)

print('-=' * 30)
print(f'A lista gerada pelo usuário é: {lista_usuario}')
print(f'A lista dos números pares é: {lista_par}')
print(f'A lista dos números ímpares é: {lista_impar}')
