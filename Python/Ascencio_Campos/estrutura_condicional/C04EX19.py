"""
Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela
a seguir, verifique e mostre a classificação dessa pessoa.

    ALTURA                            PESO    
                    ATÉ 60      ENTRE 60 E 90       ACIMA DE 90
menor que 1.2         A               D                  G
de 1.20 a 1.70        B               E                  H
maiores que 1.70      C               F                  I
             
        

"""

altura = float(input('Insira sua altura em metros: '))
peso = float(input('Insira seu peso em kg: '))

if altura < 1.2:
    if peso <= 60:
        print('Você está na classificação A.')
    elif 60 < peso <= 90:
        print('Você está na classificação D.')
    else:
        print('Você está na classificação G.')

elif 1.2 <= altura <= 1.7:
    if peso <= 60:
        print('Você está na classificação B.')
    elif 60 < peso <= 90:
        print('Você está na classificação E.')
    else:
        print('Você está na classificação H.')
    
else:
    if peso <= 60:
        print('Você está na classificação C.')
    elif 60 < peso <= 90:
        print('Você está na classificação F.')
    else:
        print('Você está na classificação I.')
    