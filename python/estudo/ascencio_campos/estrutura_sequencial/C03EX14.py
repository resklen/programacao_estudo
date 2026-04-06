"""
Faça um programa que receba o ano de nascimento de uma pessoa
e o ano atual, calcule e mostre:

a) a idade dessa pessoa
b) quantos anos ela terá em 2050

"""
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = int(input('Digite o ano atual: '))

idade = ano_atual - ano_nascimento
idade_2050 = 2050 - ano_nascimento

print(f'Sua idade é de {idade} anos.')
print(f'Em 2050 você terá {idade_2050} anos.')
