"""
Dados três valores X, Y e Z, verifique se eles podem ser os comprimentos
dos lados de um triângulo e, se forem, verifique se é um triângulo equilátero,
isósceles ou escaleno. Se eles não formarem um triângulo, escreva uma mensagem.

"""
x = float(input('Entre com o primeiro valor: '))
y = float(input('Entre com o segundo valor: '))
z = float(input('Entre com o terceiro valor: '))

if (x < (y + z)) and (y < (x + z)) and (z < (x + y)):
    if x == y == z:
        print('Os valores formam um triângulo equilátero.')
    elif x == y or x == z or y == z:
        print('Os valores formam um triângulo isósceles. ')
    else:
        print('Os valores formam um triângulo escaleno. ')

else:
    print('Não é possível formar um triângulo com esses valores. ')
