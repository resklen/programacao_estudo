"""
Faça um programa que receba o código correspondente ao cargo de um funcionário e seu
salário atual e mostre o cargo, o valor do aumento e seu novo salário. Os cargos estão
na tabela a seguir.

CÓDIGO      CARGO           PERCENTUAL
   1        Escrituário     50%
   2        Secretário      35%
   3        Caixa           20%
   4        Gerente         10%
   5        Diretor         Sem aumento
"""
codigo = int(input('''Insira o código referente ao seu cargo:
[1] Escrituário
[2] Secretário
[3] Caixa
[4] Gerente
[5] Diretor
CÓDIGO: '''))

salario = float(input('Insira seu salário: R$ '))

if codigo == 1:
    print('Seu cargo é de escrituário.')
    aumento = 0.5 * salario
    salario_novo = salario + aumento
    print(f'Você receberá um aumento de R$ {aumento:.2f} e \
seu salário passará a ser de R$ {salario_novo:.2f}')
elif codigo == 2:
    print('Seu cargo é de secretário.')
    aumento = 0.35 * salario
    salario_novo = salario + aumento
    print(f'Você receberá um aumento de R$ {aumento:.2f} e \
seu novo salário passará a ser R$ {salario_novo:.2f}')
elif codigo == 3:
    print('Seu cargo é de caixa.')
    aumento = 0.2 * salario
    salario_novo = salario + aumento
    print(f'Você receberá um aumento de R$ {aumento:.2f} e \
seu novo salário passará a ser R$ {salario_novo:.2f}')
elif codigo == 4:
    print('Seu cargo é de gerente.')
    aumento = 0.1 * salario
    salario_novo = salario + aumento
    print(f'Você receberá um aumento de R$ {aumento:.2f} e \
seu novo salário passará a ser R$ {salario_novo:.2f}')
elif codigo == 5:
    print('Seu cargo é de diretor e não receberá aumento.')
else:
    print('Código inválido')

