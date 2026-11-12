"""
CONSTANTE = "Variáveis" que não irão mudar
Muitas condições no mesmo if (ruim)
    <--- Contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 100 # local do carro na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar um está
RADAR_RANGE = 1 # a distância que o radar pega

velocidade_excedida_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_excedida_radar_1

if velocidade_excedida_radar_1:
    print('Limite de velocidade excedido no radar 1')

if carro_passou_radar_1:
    print('Carro passou pelo radar 1')

if carro_multado_radar_1:
    print('Carro multado no radar 1')