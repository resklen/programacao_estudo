from random import shuffle

primeiro_aluno = input('Digite o nome do primeiro aluno: ')
segundo_aluno = input('Digite o nome do segundo aluno: ')
terceiro_aluno = input('Digite o nome do terceiro aluno: ')
quarto_aluno = input('Digite o nome do quarto aluno: ')

lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)
