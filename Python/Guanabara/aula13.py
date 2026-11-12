# for c in range(0, 6): # para no 6 (não conta)
#     print('oi')
# print('FIM')

# for c in range(6, 0, -1): # de trás pra frente
#     print(c)
# print('FIM')

# for c in range(0, 7, 2): # pula de dois em dois até o 6
#     print (c)
# print('FIM')

# n = int(input('Digite um número: '))
# for c in range(0, n+1):
#     print(c)
# print('FIM')

# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))

# for c in range(i, f+1, p):
#     print(c)
# print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n          # s = s + n
print('O somatório de todos os valores foi {}'.format(s))
