"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foia soma entre eles (deconsiderando o flag).

"""
# cont = 0
# soma = 0
# num = 0
# while num != 999:
#     num = int(input('Digite um número [999 para parar]: '))
#     if num != 999:
#         soma += num
#         cont += 1
#     else:
#         break
# print('Você inseriu {} números, cuja soma é {}'.format(cont, soma))

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))