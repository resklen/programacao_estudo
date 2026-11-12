"""
Flag - marcar um local
None - valor nulo
is ou is not = é ou não é
id = identidade
"""
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')