"""
Faça um programa que receba quatro valores: I, A, B e C. Desses valores,
I é inteiro e positivo, A, B e C são reais. Escreva os números A, B e C
obedecendo a tabela a seguir.
Suponha que o valor digitado para I seja sempre um valor válido, ou seja,
1, 2 ou 3, e que os números digitados sejam diferentes um do outro.

VALOR DE I          FORMA A ESCREVER
    1           A, B e C em ordem crescente
    2           A, B e C em ordem decrescente
    3           O maior fica entre os outros dois números
"""
valor_a = float(input('Insira o primeiro valor: '))
valor_b = float(input('Insira o segundo valor: '))
valor_c = float(input('Insira o terceiro valor: '))
valor_i = int(input('''Insira o valor de I:
[1] para ver os números em ordem crescente
[2] para ver os números em ordem decrescente
[3] para ver o número maior entre os dois números\n'''))

if valor_i == 1:
    if valor_a < valor_b and valor_a < valor_c:
        if valor_b < valor_c:
            print(f'A ordem crescente dos valores é: {valor_a}, {valor_b} e {valor_c}')
        else:
            print(f'A ordem crescente dos valores é: {valor_a}, {valor_c} e {valor_b}')
    
    elif valor_b < valor_a and valor_b < valor_c:
        if valor_a < valor_c:
            print(f'A ordem crescente dos valores é: {valor_b}, {valor_a} e {valor_c}')
        else:
            print(f'A ordem crescente dos valores é: {valor_b}, {valor_c} e {valor_a}')
        
    elif valor_c < valor_a and valor_c < valor_b:
        if valor_a < valor_b:
            print(f'A ordem crescente dos valores é: {valor_c}, {valor_a} e {valor_b}')
        else:
            print(f'A ordem crescente dos valores é: {valor_c}, {valor_b} e {valor_a}')

elif valor_i == 2:
    if valor_a > valor_b and valor_a > valor_c:
        if valor_b > valor_c:
            print(f'A ordem decrescente dos valores é: {valor_a}, {valor_b} e {valor_c}')
        else:
            print(f'A ordem decrescente dos valores é: {valor_a}, {valor_c}, {valor_b}')
    
    elif valor_b > valor_a and valor_b > valor_c:
        if valor_a > valor_c:
            print(f'A ordem decrescente dos valores é: {valor_b}, {valor_a} e {valor_c}')
        else:
            print(f'A ordem decrescente dos valores é: {valor_b}, {valor_c} e {valor_a}')
    
    elif valor_c > valor_a and valor_c > valor_b:
        if valor_a > valor_b:
            print(f'A ordem decrescente dos valores é: {valor_c}, {valor_a} e {valor_b}')
        else:
            print(f'A ordem decrescente dos valores é: {valor_c}, {valor_b} e {valor_a}')

elif valor_i == 3:
    if valor_a > valor_b and valor_a > valor_c:
        if valor_b > valor_c:
            print(f'A ordem, com o maior no meio, é: {valor_c}, {valor_a} e {valor_b}')
        else:
            print(f'A ordem, com o maior no meio, é: {valor_b}, {valor_a} e {valor_c}')
    
    elif valor_b > valor_a and valor_b > valor_c:
        if valor_a > valor_c:
            print(f'A ordem, com o maior no meio, é: {valor_c}, {valor_b} e {valor_a}')
        else:
            print(f'A ordem, com o maior no meio, é: {valor_a}, {valor_b} e {valor_c}')
    
    elif valor_c > valor_a and valor_c > valor_b:
        if valor_a > valor_b:
            print(f'A ordem, com o maior no meio, é: {valor_b}, {valor_c} e {valor_a}')
        else:
            print(f'A ordem, com o maior no meio, é: {valor_a}, {valor_c} e {valor_b}')

else:
    print('O valor de I só pode ser 1, 2 ou 3. ')
