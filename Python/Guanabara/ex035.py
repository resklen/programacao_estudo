"""
Desenvolva um programa que leia o comprimento de três
retas e diga ao usuário se elas podem ou não formar um
triângulo.
"""
lado1 = float(input('Digite o comprimento em m do primeiro lado: '))
lado2 = float(input('Digite o comprimento em m do segundo lado: '))
lado3 = float(input('Digite o comprimento em m do terceiro lado: '))

condicao1 = lado1 < (lado2 + lado3)
condicao2 = lado2 < (lado1 + lado3)
condicao3 = lado3 < (lado1 + lado2)

if condicao1 and condicao2 and condicao3:
    print('As retas de comprimento {} m, {} m e {} m podem formar um triângulo.'.format(lado1, lado2, lado3))
else:
    print('As retas de comprimento {} m, {}m e {} m não podem formar um triângulo'.format(lado1, lado2, lado3))

