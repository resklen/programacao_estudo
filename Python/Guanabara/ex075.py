"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9;

B) Em qual posição foi digitado o valor 3;

C) Quais foram os números pares.

"""
primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
terceiro = int(input('Digite o terceiro valor: '))
quarto = int(input('Digite o quarto valor: '))

valores = (primeiro, segundo, terceiro, quarto)


nove = 0
print(f'Os valores digitados foram: {valores}')
for cont in valores:
    if cont == 9:
        nove += 1
print(f'O número nove apareceu {nove} vezes. ')
print(f'O número nove apareceu {valores.count(9)} vezes')

if 3 in valores:
    print(f'O número três apareceu na {valores.index(3) + 1}ª posição')
else:
    print('Não foi digitado nenhum valor igual a três.')

print('Os números pares são: ', end='')
for numero in valores:
    if numero % 2 == 0:
        print(numero, end =' ')
   
