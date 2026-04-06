"""
Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos,
para os quais fornece a quantidade de ração em gramas. A quantidade diária
de ração fornecida para cada gato é sempre a mesma. Faça um programa que
receba o peso do saco de ração e a quantidade de ração fornecida para cada
gato, calcule e mostre quanto restará de ração no saco após cinco dias.

"""
quant_saco_kg = float(input('Insira o peso do saco de ração em kg: '))
quant_racao_primeiro_gato = float(input('Insira a quantidade de ração fornecida (g) para o primeiro gato: '))
quant_racao_segundo_gato = float(input('Insira a quantidade de ração fornecida (g) para o segundo gato: '))

quant_saco_g = quant_saco_kg * 1000
quantidade_racao_diaria = quant_racao_primeiro_gato + quant_racao_segundo_gato
quant_racao_restante = quant_saco_g - quantidade_racao_diaria * 5

print(f'A quantidade de ração restante, após cinco dias, é de {quant_racao_restante:.2f} g')
