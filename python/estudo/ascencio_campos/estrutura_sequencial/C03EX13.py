"""
Sabe-se que:
pé = 12 polegadas
1 jarda = 3 pés
1 milha = 1760 jarda

Faça um programa que receba uma medida em pés, faça as conversões 
a seguir e mostre os resultados.

a) polegadas;
b) jardas;
c) milhas.

"""
medida_pes = float(input('Insira o valor da medida em pés: '))

medida_polegadas = medida_pes * 12
medida_jardas = medida_pes / 3
medida_milhas = medida_jardas / 1760

print(f'{medida_pes} pés equivalem a {medida_polegadas:.2f} polegadas.')
print(f'{medida_pes} pés equivalem a {medida_jardas:.2f} jardas.')
print(f'{medida_pes} pés equivalem a {medida_milhas:.4f} milhas.')
