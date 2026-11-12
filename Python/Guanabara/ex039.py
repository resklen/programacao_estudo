"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
# ano_atual = int(input('Digite o ano atual: '))
# ano_nasc = int(input('Digite seu ano de nascimento: '))

# idade = ano_atual - ano_nasc
# condicao_alistamento = idade == 17
# condicao_nao = idade < 17
# falta = 17 - idade
# passou = idade - 17

# if condicao_alistamento:
#     print('É a hora exata de se alistar no programa militar!')
# elif condicao_nao:
#     print('Ainda não é a hora de você se alistar, faltam {}.'.format(falta))
# else:
#     print('Já passaram {} anos da hora de você se alistar.'.format(passou))

from datetime import date
sexo = str(input('Você é homem ou mulher?')).upper()

if sexo == 'HOMEM':
    atual = date.today().year
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc

    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

    if idade == 18:
        print('Você tem que se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print('Você ainda não tem 18 anos, faltam {} anos para você se alistar'.format(saldo))
        print('Seu alistamento será em {}'.format(ano))
    else:
        saldo = idade - 18
        ano = atual - saldo
        print('Já passaram {} anos da hora de você se alistar.'.format(saldo))
        print('Seu alistamento foi em {}'.format(ano))
elif sexo == 'MULHER':
    print('Você não precisa se alistar.')
else:
    print('Sexo inválido.')
