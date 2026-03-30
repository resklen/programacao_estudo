"""
Crie uma tupla preenchida com os 20 primeiros colocados do campeonato
brasileiro de futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times

b) Os últimos 4 colocados

c) Times em ordem alfabética

d) Em qual posição está o time da Chapecoense

"""

tabela = ('Palmeiras', 'Athletico-PR', 'São Paulo', 'Fluminense',
          'Flamengo', 'Bahia', 'Coritiba', 'Grêmio', 'Vasco', 'Vitória',
          'Corinthians', 'Internacional', 'Atlético-MG', 'Bragantino',
          'Chapecoense', 'Santos', 'Botafogo', 'Mirassol', 'Remo',
          'Cruzeiro.')
    

print(f'Os cinco primeiros colocados são: {tabela[:5]}')
print('-=' * 20)
print(f'Os quatro últimos colocados são: {tabela[-4:]}')
print('-=' * 20)
print(f'Os times, em ordem alfabética, são: {sorted(tabela)}')
print('-=' * 20)
print(f'A chapecoense está na {tabela.index('Chapecoense') + 1}ª posição')
