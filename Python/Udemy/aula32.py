"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero_inteiro_str = input('Digite um número inteiro: ')

# try: # poderia usar numero_inteiro_str.isdigit()
#     numero_inteiro_int = int(numero_inteiro_str)
#     resto = numero_inteiro_int % 2
#     numero_par = resto == 0
#     if numero_par:
#         print('Número par.')
#     else:
#         print('Número ímpar.')
# except:
#     print('Você não digitou um número inteiro.')

# if numero_par:
#     print('Você digitou um número par.')
# elif numero_impar:
#     print('Você digitou um número ímpar.')
# else:
#     print('Você não digitou um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora_str = input('Digite a hora: ')
# try:

#     hora_int = int(hora_str)
#     bom_dia = (hora_int >= 0) and (hora_int <= 11)
#     boa_tarde = (hora_int >= 12) and (hora_int <= 17)
#     boa_noite = (hora_int >= 18) and (hora_int <= 23)

#     if bom_dia:
#         print('Bom dia.')
#     elif boa_tarde:
#         print('Boa tarde.')
#     elif boa_noite:
#         print('Boa noite')
#     else:
#         print('Número inválido')
# except:
#     print('Você não digitou um valor válido para a hora.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')
letras_qtd = len(nome)
nome_curto = (letras_qtd >= 1) and (letras_qtd <= 4)
nome_normal = (letras_qtd >= 5) and (letras_qtd <= 6)
nome_grande = (letras_qtd > 6)

if nome_curto:
    print('Seu nome é curto.')
elif nome_normal:
        print('Seu nome é normal')
else:
        print('Seu nome é muito grande')
