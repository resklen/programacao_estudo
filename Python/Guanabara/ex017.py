import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

soma_quad = math.pow(co, 2) + math.pow(ca, 2)
hip1 = math.sqrt(soma_quad)
hip2 = math.hypot(co, ca)

print('O valor da hipotenusa é {:.2f}.'.format(hip1))
print('O valor da hipotenusa é {:.2f}.'.format(hip2))