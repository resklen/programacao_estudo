"""
Refaça o exercício 35 dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados são iguais
- ISÓSCELES: dois lados iguais e um diferente
- ESCALENO: todos os lados diferentes
"""
lado1 = float(input('Digite o comprimento em m do primeiro lado: '))
lado2 = float(input('Digite o comprimento em m do segundo lado: '))
lado3 = float(input('Digite o comprimento em m do terceiro lado: '))

condicao1 = lado1 < (lado2 + lado3)
condicao2 = lado2 < (lado1 + lado3)
condicao3 = lado3 < (lado1 + lado2)

if condicao1 and condicao2 and condicao3:
    equilatero = lado1 == lado2 and lado1 == lado3                  # O python também aceitaria lado1 == lado2 == lado3.
    isosceles = lado1 == lado2 or lado1 == lado3 or lado2 == lado3  # Poderia ficar no else.
    if equilatero:
        print('As retas de comprimento {} m, {} m e {} m ' \
        'formam um triângulo EQUILÁTERO'.format(lado1, lado2, lado3))
    elif isosceles:
        print('As retas de comprimento {} m, {} m e {} m ' \
        'formam um triângulo ISÓSCELES'.format(lado1, lado2, lado3))
    else:                                                            # O python também aceitaria lado1 != lado2 != lado3 != lado1 para escaleno    
        print('As retas de comprimento {} m, {} m, {} m ' \
        'formam um triângulo ESCALENO'.format(lado1, lado2, lado3))
else:
    print('As retas de comprimento {} m, {} m, e {} m ' \
    'não podem formar um triângulo'.format(lado1, lado2, lado3))
