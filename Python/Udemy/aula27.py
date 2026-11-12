"""
FATIAMENTO DE STRINGS

 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[:4]) # omitir início começa no 0, omitir fim vai até o último caractere
print(len(variavel))
print(variavel[0:len(variavel):2])
print(variavel[::-1])