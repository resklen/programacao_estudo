"""
Faça um programa que receba três números obrigatoriamente em ordem crescente
e um quarto número que náo siga essa regra. Mostre, em seguida, os quatro números
em ordem decrescente. Suponha que o usuário digitará quatro números diferentes.

"""
primeiro_numero = float(input('Insira três valores em ordem crescente.\nInsira o primeiro valor: '))
segundo_numero = float(input('Insira o segundo valor: '))
if segundo_numero <= primeiro_numero:
    print('Os números devem estar em ordem crescente. ')
else:
    terceiro_numero = float(input('Insira o terceiro valor: '))
    if terceiro_numero <= segundo_numero:
        print('Os números devem estar em ordem crescente. ')
    else:
        quarto_numero = float(input('Insira um quarto valor: '))

        if quarto_numero > terceiro_numero and quarto_numero not in (primeiro_numero, segundo_numero, terceiro_numero):

            print(f'A ordem decrescente desses números é: {quarto_numero, terceiro_numero, segundo_numero, primeiro_numero}')
        elif quarto_numero < terceiro_numero and quarto_numero > segundo_numero:
            print(f'A ordem decrescente desses números é : {terceiro_numero, quarto_numero, segundo_numero, primeiro_numero}')
        elif quarto_numero < segundo_numero and quarto_numero > primeiro_numero:
            print(f'A ordem decrescente desses números é: {terceiro_numero, segundo_numero, quarto_numero, primeiro_numero}')
        elif quarto_numero < primeiro_numero:
            print(f'A ordem decrescente desses números é: {terceiro_numero, segundo_numero, primeiro_numero, quarto_numero}')
        else:
            print('O quarto número deve ser diferente dos outros.')
            





# ordem = []

# primeiro_numero = float(input('Insira, em ordem crescente, o primeiro valor: '))
# ordem.append(primeiro_numero)
# segundo_numero = float(input('Insira, em ordem crescente, o segundo valor: '))
# if segundo_numero > primeiro_numero:
#     ordem.append(segundo_numero)
#     terceiro_numero = float(input('Insira, em ordem crescente, o terceiro valor: '))
#     if terceiro_numero > segundo_numero:
#         ordem.append(terceiro_numero)
#         quarto_numero = float(input('Insira um quarto valor: '))
#         ordem.append(quarto_numero)
#         ordem.sort(reverse=True)
#         print(f'Os quatro números, em ordem decrescente, são: {ordem}')

#     else:
#         print('Os números devem estar em ordem crescente. ')
# else:
#     print('Os números devem estar em ordem crescente. ')

