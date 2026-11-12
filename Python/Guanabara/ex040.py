"""
Crie um programa que leia duas notas de um aluno e calcula
sua média, mostrando uma mensagem no final, de acordo com 
a média atingida
"""
n1 = float(input('Valor da primeira nota: '))
n2 = float(input('Valor da segunda nota: '))

media = (n1 + n2) / 2
aprovado = media >= 7.0
recuperacao = media >= 5 and media < 7

if aprovado:
    print('Sua média é {:.2f}, você está APROVADO!'.format(media))
elif recuperacao:
    print('Sua média é {:.2f}, você está de RECUPERAÇÃO!'.format(media))
else:
    print('Sua média é {:.2f}, você está REPROVADO!.'.format(media))
