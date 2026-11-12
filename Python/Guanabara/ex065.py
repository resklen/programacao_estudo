"""
Crie um programa que leia varios numeros inteiros pelo teclado.
No final da execucao, mostre a media entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar ao
usuario se ele quer ou nao continuar a digitar valores.
"""

continua = 'S'
soma = 0
cont = 0

while continua != 'N':
    numero = int(input('Digite um numero inteiro: '))

    if cont == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    soma += numero
    cont += 1
    media = soma / cont
    continua = str(input('Quer continuar? [S/N]: ')).upper()

print('A media dos valores digitados e {}.'.format(media))
print('O maior valor foi {}'.format(maior))
print('O menor valor foi {}'.format(menor))
