"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
print('{:=^40}'.format(' LOJAS MORAES '))
valor = float(input('Digite o preço das compras: R$'))
opcao = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção?\n'''))

dinheiro = valor - 0.10 * valor
cartao = valor - 0.05 * valor
# Opcao 3 -> preço normal

juros = 0.20 * valor
tres_vezes = juros / 3

if opcao == 1:
    novo_valor = dinheiro
    print('Você recebeu 10% de desconto e deverá pagar R${:.2f}.'.format(novo_valor))
elif opcao == 2:
    novo_valor = cartao
    print('Você recebeu 5% de desconto e deverá pagar R${:.2f}.'.format(novo_valor))
elif opcao == 3:
    duas_vezes = valor / 2
    print('Você poderá pagar RS{:.2f}, em 2x de R${:.2f}.'.format(valor, duas_vezes))
elif opcao == 4:
    novo_valor = valor + juros
    nvezes = int(input(f'O novo valor é R${novo_valor}, em quantas vezes quer fazer?\n'))
    parcela = novo_valor / nvezes
    print('Você deverá pagar R${:.2f}, em {}x de R${:.2f}'.format(novo_valor, nvezes, parcela))
else:
    print('Opção inválida.')
