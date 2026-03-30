"""
Crie um programa que tenha uma dupla totalmente preenchida com uma
contagem por extenso, de zero até 20. Seu programa deverá ler um 
número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

"""

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
            'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
            'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))

    if numero in range(0, len(contagem)):
        print(f'Você digitou o número {contagem[numero]}')
        break
    else:
        print('Valor incorreto. Tente novamente. ')
