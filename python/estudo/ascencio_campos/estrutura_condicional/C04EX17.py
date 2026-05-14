"""
Faça um programa para resolver equações do 2º grau:

"""
from math import sqrt
print('Seguindo o formato ax² + bx + c = 0')
a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = pow(b, 2) - (4 * a * c)

if a == 0:
    print('Essa não é uma equação do segundo grau. ')

else:
    if delta > 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print(f'O valor de x é {x1} ou {x2}')
    elif delta == 0:
        x = (-b) / (2 * a)
        print(f'O valor de x é {x}')
    else:
        print('As raízes da equação não pertence ao conjunto dos números reais.')
          