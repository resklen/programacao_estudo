"""
Faça um programa que mostre o menu de opções a seguir, receba a opção do usuário
e os dados necessários para executar cada operação.

Menu de opções:
1. Somar dois números.
2. Raiz quadrada de um número.

Digite a opção desejada:

"""
from math import sqrt
opcao = int(input('''Menu de opções:
1. Somar dois números.
2. Raiz quadrada de um número.\n'''))

if opcao == 1:
    primeiro_numero = float(input('Insira o primeiro valor: '))
    segundo_numero = float(input('Insira o segundo valor: '))

    soma = primeiro_numero + segundo_numero

    print(f'A soma entre {primeiro_numero} e o {segundo_numero} vale {soma}')

elif opcao == 2:
    numero = float(input('Insira um número: '))

    raiz = sqrt(numero)

    print(f'A raiz quadrada de {numero} vale {raiz:.2f}')

else:
    print('Opção inválida. ')
