primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

cont = 1
mais = 10
termo = primeiro
ntermos = 0

while mais != 0:
    ntermos = ntermos + mais
    while cont <= ntermos:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
        print('termo = {}, cont = {}, ntermos = {}'.format(termo, cont, ntermos))
    
    mais = int(input('PAUSA...\n Quantos números quer digitar a mais? '))

print('Progressão finalizada com {} termos mostrados'.format(ntermos))