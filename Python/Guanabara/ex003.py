""" Somando dois números """
n1 = input('\033[1;32mDigite um número: \033[m')
n2 = input('\033[1;35mDigite outro número: \033[m')

n1_int = int(n1)
n2_int = int(n2)

soma = n1_int + n2_int
sublinha = '\033[4m'
limpa = '\033[m'

print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}'.format('\033[4m',n1,'\033[m','\033[4m', n2,'\033[m', '\033[4m', soma, '\033[m'))

print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}'.format(sublinha, n1, limpa, sublinha, n2, limpa, sublinha, soma, limpa))
