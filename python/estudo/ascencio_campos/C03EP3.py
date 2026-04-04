"""
Faça um programa que receba dois números, calcule e mostre a divisão
do primeiro número pelo segundo. Sabe-se que o segundo número não pode
ser zero, portanto, não é necessário se preocupar com validações.

"""
primeiro_numero = float(input('Insira o primeiro número: '))
segundo_numero = float(input('Insira o segundo número: '))

divisao = primeiro_numero / segundo_numero

print(f'A divisão do {primeiro_numero} pelo {segundo_numero} é igual a {divisao}')
