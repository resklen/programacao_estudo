"""
Refaça o desafio 9, mostrando a tabuada de um número que o
usuário escolher, só que agora utilizando o laço for

"""
# MINHA RESOLUÇÃO
# n = int(input('Quer saber a tabuada de qual número? '))
# c = 1
# m = n
# for c in range(1, 11):
#     print('{} x {} = {}'.format(n, c, m))
#     m = n + n * c
#     c += 1

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
