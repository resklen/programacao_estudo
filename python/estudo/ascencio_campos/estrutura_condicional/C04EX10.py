"""
Faça um programa que determine a data cronologicamente maior entre duas datas fornecidas
pelo usuário. Cada data deve ser composta por três valores inteiros, em que o primeiro
representa o dia, o segundo, o mês e o terceiro, o ano.

"""
dia_primeiro = int(input('Insira o dia da primeira data (dd): '))
mes_primeiro = int(input('Insira o mês da primeira data (mm): '))
ano_primeiro = int(input('Insira o ano da primeira data (aaaa): '))

dia_segundo = int(input('Insira o dia da segunda data (dd): '))
mes_segundo = int(input('Insira o mês da segunda data (mm): '))
ano_segundo = int(input('Insira o ano da segunda data (aaaa): '))

if ano_primeiro > ano_segundo:
    print(f'A data cronologicamente maior é: {dia_primeiro}/{mes_primeiro}/{ano_primeiro}')
elif ano_segundo > ano_primeiro:
    print(f'A data cronologicamente maior é: {dia_segundo}/{mes_segundo}/{ano_segundo}')
else:
    if mes_primeiro > mes_segundo:
        print(f'A data cronologicamente maior é: {dia_primeiro}/{mes_primeiro}/{ano_primeiro}')
    elif mes_segundo > mes_primeiro:
        print(f'A data cronologicamente maior é: {dia_segundo}/{mes_segundo}/{ano_segundo}')
    else:
        if dia_primeiro > dia_segundo:
            print(f'A data cronologicamente maior é: {dia_primeiro}/{mes_primeiro}/{ano_primeiro}')
        elif dia_segundo > dia_primeiro:
            print(f'A data cronologicamente maior é: {dia_segundo}/{mes_segundo}/{ano_segundo}')
        else:
            print('As datas são iguais.')

