"""
Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar

[2] multiplicar

[3] maior

[4] digitar novos números

[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.

"""
from time import sleep
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
menu = False
while not menu:
    
    print('-=' * 13)
    opcao = int(input('''Escolha o que quer fazer:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] inserir novos números
[ 5 ] sair do programa\n'''))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} com {} é {}'.format(n1, n2, soma))

    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, mult))

    elif opcao == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        elif n1 < n2:
            print('O maior número é {}'.format(n2))
        else:
            print('Os números são iguais.')
    
    elif opcao == 4:
       n1 = int(input('Digite o primeiro número: '))
       n2 = int(input('Digite o segundo número: '))

    elif opcao == 5:
        break

    else: 
        print('Opção inválida.')
    sleep(2)
