"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

"""
from datetime import date 
maior = 0
menor = 0
ano_atual = date.today().year
for p in range(1, 8):
    
    ano_nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(p)))
    idade = ano_atual - ano_nasc
    
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('{} pessoas atingiram a maioridade.'.format(maior))
print('{} pessoas não atingiram a maioridade.'.format(menor))
