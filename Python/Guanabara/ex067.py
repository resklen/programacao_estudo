"""
Faça um programa que mostre a tabuada de vários números, um de cada
vez, para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo.

"""
cont = 1
while True:

    num = int(input('Digite um número para ver sua tabuada: '))
    print('-=' * 15)
    if num < 0:
        break    
    for cont in range(1, 11):
        print(f'{num} X {cont} = {num * cont}')
    print('-=' * 15)
print('Programa encerrado. ')

    