"""
Um supermercado deseja reajustar o preço de seus produtos usando o seguinte critério:
o produto poderá ter seu preço aumentado ou diminuído. Para o preço ser alterado, o 
produto deve preencher pelo menos um dos requisitos a seguir:

VENDA MÉDIA MENSAL              PREÇO ATUAL             % DE AUMENTO                % DE DIMINUIÇÃO
    < 500                     < R$ 30.00                  10                              -
>= 500 e < 1200               >= R$ 30.00 e < R$ 80.00    15                              -
    >= 1200                   >= R$ 80.00                 -                               20

"""

preco_atual = float(input('Insira o preço atual do produto: R$ '))
venda_mensal = float(input('Insira a venda média mensal desse produto: '))

if venda_mensal < 500 or preco_atual < 30:
    preco_final = 1.10 * preco_atual

elif (venda_mensal >= 500 and venda_mensal < 1200) or (preco_atual >= 30 and preco_atual < 80):
    preco_final = 1.15 * preco_atual

else:
    preco_final = 0.8 * preco_atual

    
print(f'O valor reajustado do produto é R$ {preco_final:.2f}')
