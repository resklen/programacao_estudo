# from math import floor
# num = float(input('Digite um número real: '))
# print('O valor digitado foi {} e sua porção inteira é {}.'.format(num, floor(num)))

from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))
