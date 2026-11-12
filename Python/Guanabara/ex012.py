preco = float(input('Digite o valor do produto em real: '))

novo_preco = preco - 0.05 * preco

print('O produto que custava R${:.2f}, com desconto custará R${:.2f}'.format(preco, novo_preco))
