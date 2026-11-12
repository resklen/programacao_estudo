"""
A nota final de um estudante é calculada a partir de três notas atribuídas,
respectivamente, a um trabalho de laboratório (peso 2), a uma avaliação semestral (peso 3) e 
a um exame final (peso 5).
Faça um programa que receba as três notas, calcule e mostre a média ponderada e o conceito
que segue a baixo:

Conceito A: 8 <= média <= 10
Conceito B: 7 <= média < 8 
Conceito C: 6 <= média < 7
Conceito D: 5 <= média < 6
Conceiro E: 0 <= média < 5

"""

nota_trabalho = float(input('Insira a nota do trabalho de laboratório: '))
nota_avaliacao = float(input('Insira a nota da avaliação semestral: '))
nota_exame = float(input('Insira a nota do exame: '))

media = ((nota_trabalho * 2) + (nota_avaliacao * 3) + (nota_exame * 5)) / 10

if media >= 8 and media <= 10:
    print(f'Sua média é {media:.1f} (conceito A)')
elif media >= 7 and media < 8:
    print(f'Sua média é {media:.1f} (conceito B)')
elif media >= 6 and media < 7:
    print(f'Sua média é {media:.1f} (conceito C)')
elif media >= 5 and media < 6:
    print(f'Sua média é {media:.1f} (conceito D)')
elif media < 5:
    print(f'Sua média é {media:.1f} (conceito E)')
