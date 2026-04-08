"""
Faça um programa que receba três notas de um aluno, calcule e mostre
a média e a mensagem constante na tabela a seguir. Aos
alunos que ficaram de recuperação, calcule e mostre a nota que deverão
tirar para serem aprovados, considerando que a média exigida é 5.0.

0 <= media < 3: Reprovado
3 <= media < 5: Recuperação
5 <= media <= 10: Aprovado

"""
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))

media = (nota1 + (nota2 * 2) + (nota3 * 2)) / 5

nota_recuperação = 10 - media

if media >= 5 and media <= 10:
    print(f'Sua média é {media:.1f} e você está APROVADO')
elif media >= 3 and media < 5:
    nota_recuperação = 10 - media
    print(f'Sua média é {media:.1f} e deverá tirar {nota_recuperação:.1f} na recuperação \
para ser aprovado.')
elif media < 3:
    print('Você está reprovado.')

