"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas 
respectivas posições na lista.

"""
# valores = []

# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))

# maior = max(valores)
# menor = min(valores)
# posicao_maior = valores.index(maior) + 1
# posicao_menor = valores.index(menor)+ 1

# print(f'Você digitous os valores {valores}. ')
# print(f'O maior valor é {maior} e está na posição {posicao_maior}. ')
# print(f'O menor valor é {menor} e está na posição {posicao_menor}. ')

valores = list()
maior = 0
menor = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite o valor da posição {c}: ')))

    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print('=-' * 30)
print(f'Você digitou os valores: {valores}. ')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, valor in enumerate(valores):
    if valor == maior:
        print(f'{i}... ', end='')
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, valor in enumerate(valores):
    if valor == menor:
        print(f'{i}... ', end='')
