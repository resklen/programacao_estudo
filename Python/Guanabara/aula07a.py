# nome = input('Qual é o seu nome? ')
# print('Prazer em te conhecer {:=^20}!'.format(nome))
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2

print('A soma é {},\n o produto é {}\n a divisão é {:.3f}'.format(s, m, d), end='  ')
print('A potência é {},\n a divisão inteira é {}\n e o resto é {}'.format(e, di, r))
