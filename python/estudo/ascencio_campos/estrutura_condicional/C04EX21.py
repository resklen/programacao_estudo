"""
Faça um programa que receba:
- o código do estado de origem da carga de um caminhão, supondo que a digitação
do código do estado seja sempre válida, isto é, um número inteiro entre 1 e 5;
- o peso da carga do caminhão em toneladas;
- o código da carga, supondo que a digitação do código seja sempre válida, isto é,
um número inteiro entre 10 e 40.

    CÓDIGO DO ESTADO        IMPOSTO
            1                 35%
            2                 25%
            3                 15%
            4                 5%
            5                isento

    CÓDIGO DA CARGA         PREÇO POR QUILO
        10 a 20                 100
        21 a 30                 250
        31 a 40                 340

Calcule e mostre:
- o peso da carga do caminhão convertido em quilos;
- o preço da carga do caminhão;
- o valor do imposto, sabendo que o imposto é cobrado sobre o preço da carga do caminhão
e depende do estado de origem;
- o valor total transportado pelo caminhão, preço da carga mais imposto.

"""

codigo_origem = int(input('Insira o código do estado de origem da carga: '))
peso_ton = float(input('Insira do peso da carga do caminhão em toneladas: '))
codigo_carga = int(input('Insira o código da carga: '))

peso_quilos = peso_ton * 1000

if codigo_carga >= 10 and codigo_carga <= 20:
    preco_carga = 100 * peso_quilos

elif codigo_carga >= 21 and codigo_carga <= 30:
    preco_carga = 250 * peso_quilos

elif codigo_carga >= 31 and codigo_carga <= 40:
    preco_carga = 340 * peso_quilos

if codigo_origem == 1:
    imposto = 0.35 * preco_carga

elif codigo_origem == 2:
    imposto = 0.25 * preco_carga

elif codigo_origem == 3:
    imposto = 0.15 * preco_carga

elif codigo_origem == 4:
    imposto = 0.05 * preco_carga

elif codigo_origem == 5:
    imposto = 0

valor_total = preco_carga + imposto

print(f'O peso do caminhão, em quilos, é de {peso_quilos:.2f} kg')
print(f'O preço da carga do caminhão é de R$ {preco_carga:.2f}')
print(f'O valor do imposto cobrado é de R$ {imposto:.2f}')
print(f'O valor total transportado pelo caminhão é de R$ {valor_total:.2f}')

