"""
Um trabalhador recebeu seu salário e o depositou em sua conta bancária.
Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual.
Sabe-se que cada operação bancária de retirada paga CPMF de 0.38% e o saldo
inicial da conta está zerado.

"""

salario_inicial = float(input('Insira o valor do seu salário: R$'))
primeiro_cheque = float(input('Insira o valor do primeiro cheque: R$'))
segundo_cheque = float(input('Insira o valor do segundo cheque: R$'))

valor_primeiro_cpmf = 0.0038 * primeiro_cheque
saldo_parcial = salario_inicial - primeiro_cheque - valor_primeiro_cpmf 
valor_segundo_cpmf = 0.0038 * segundo_cheque 
saldo_total = saldo_parcial - segundo_cheque - valor_segundo_cpmf

print(f'O valor pago do primeiro CPMF foi de R${valor_primeiro_cpmf:.2f}')
print(f'O valor pago do segundo CPMF foi de R${valor_segundo_cpmf:.2f}')
print(f'O saldo atual da sua conta é de R${saldo_total:.2f}')
