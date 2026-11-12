numero = int(input('Digite um número: '))

resto = numero % 2

if resto == 0:
    print('{} é par.'.format(numero))
else:
    print('{} é ímpar.'.format(numero))
