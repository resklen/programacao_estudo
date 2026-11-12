"""
Crie um programa que leia uma frase qualquer e diga se ela
é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
ANOTARAM A DATA DA MARATONA

"""
print('-=' * 11)
print('DETECTOR DE PALÍNDROMO')
print('-=' * 11)

frase = str(input('Digite uma frase: ')).upper().strip() # strip elimina os espaços

palavras = frase.split()
junto = ''.join(palavras)

inverso = junto[::-1]

""""inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]"""

print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('A frase não é um palíndromo.')
