"""
Sabe-se que, para iluminar de maneira correta os cômodos de uma casa,
para cada m², deve-se usar 18 W de potência. Faça um programa que
receba duas dimensões de um cômodo (em metros), calcule e mostre
a sua área (em m²) e a potência de iluminação que deverá ser utilizada.

"""
comprimento = float(input('Insira o comprimento do cômodo (em metros): '))
largura = float(input('Insira a largura do cômodo (em metros): '))

area = comprimento * largura

potencia = 18 * area

print(f'Deverá ser instalado {potencia:.2f} W de potência para iluminar \
uma área de {area:.2f} m²')
