"""
A confederação nacional de natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""
from datetime import date

ano_nasc = int(input('Digite seu ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano_nasc
mirim = idade <= 9
infantil = idade > 9 and idade <= 14
junior = idade > 14 and idade <= 19
senior = idade > 19 and idade <= 25

if mirim:
    print('Sua idade é {} e você pertence à categoria MIRIM.'.format(idade))
elif infantil:
    print('Sua idade é {} e você pertence à categoria INFANTIL.'.format(idade))
elif junior:
    print('Sua idade é {} e você pertence à categoria JUNIOR.'.format(idade))
elif senior:
    print('Sua idade é {} e você pertence à categoria SENIOR.'.format(idade))
else:
    print('Sua idade é {} e você pertence à categoria MASTER'.format(idade))
