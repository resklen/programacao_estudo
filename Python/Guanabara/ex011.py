largura = float(input('Digite a largura da parede em metro: '))
altura = float(input('Digite a altura da parede em metro: '))

area = largura * altura
qtd_tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, area))
print(f'Você precisará de {qtd_tinta:.2f} L de tinta')
