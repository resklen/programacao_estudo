"""
Crie um programa onde o usuários digite uma expressão qualquer que
use parênteses. Seu aplicativo deverá analisar se a expressão passada
está com os parênteses abertos e fechados na ordem correta.

"""

expressao = str(input('Digite a expressão: '))
pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:      # Cada parênteses que abriu fechou
    print('Sua expressão está válida. ')
else:
    print('Sua expressão está inválida. ')
