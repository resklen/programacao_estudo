"""
Faça um programa que apresente o menu a seguir, permita ao usuário a escolher a
opção desejada, receba os dados necessários para executar a operação e mostre o
resultado. Verifique a possibilidade de opção inválida e não se preocupe com 
restrições, como salário negativo

Menu de opções:
1. Imposto
2. Novo salário
3. Classificação

"""

opcao = int(input('''Menu de opções:
[1] Imposto
[2] Novo salário
[3] Classificação
Insira a opção desejada: '''))

if opcao == 1:
    salario = float(input('Insira seu salário: R$ '))

    if salario > 850:
        imposto = 0.15 * salario
        print(f'O imposto é de R$ {imposto:.2f}')
    
    elif salario >= 500 and salario <= 850:
        imposto = 0.10 * salario
        print(f'O imposto é de R$ {imposto:.2f}')
    
    elif salario < 500:
        imposto = 0.05 * salario
        print(f'O imposto é de R$ {imposto:.2f}')

elif opcao == 2:
    salario = float(input('Insira seu salário: R$ '))

    if salario > 1500:
        novo_salario = salario + 25
        print(f'Seu novo salário será de R$ {novo_salario:.2f}')
    
    elif salario >= 750 and salario <= 1500:
        novo_salario = salario + 50
        print(f'Seu novo salário será de R$ {novo_salario:.2f}')
    
    elif salario >= 450 and salario < 750:
        novo_salario = salario + 75
        print(f'Seu novo salário será de R$ {novo_salario:.2f}')
    
    elif salario < 450:
        novo_salario = salario + 100
        print(f'Seu novo salário será de R$ {novo_salario:.2f}')
    
elif opcao == 3:
    salario = float(input('Insira seu salário: R$ '))

    if salario > 700:
        print('Você é classificado como bem remunerado.')
    
    elif salario <= 700:
        print('Você é classificado como mal remunerado.')

else:
    print('Opção inválida.')
