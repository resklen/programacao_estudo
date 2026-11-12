"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
seu IMC e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: abaixo do peso
- IMC entre 18,5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- Acima de 40: obesidade mórbida
"""
print('-=' * 18)
print('\tCALCULADORA DE IMC')
print('-=' * 18)

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))

imc = peso / pow(altura, 2)

abaixo = imc < 18.5
ideal = imc >= 18.5 and imc < 25
sobrepeso = imc >= 25 and imc < 30
obeso = imc >= 30 and imc < 40

if abaixo:
    print('Seu IMC é {:.2f} kg/m². Você está abaixo do peso.'.format(imc))
elif ideal:
    print('Seu IMC é {:.2f} kg/m². Você está no peso ideal.'.format(imc))
elif sobrepeso:
    print('Seu IMC é {:.2f} kg/m². Você está com sobrepeso.'.format(imc))
elif obeso:
    print('Seu IMC é {:.2f} kg/m². Você está obeso.'.format(imc))
else:
    print('Seu IMC é {:.2f} kg/m². Você está com obesidade mórbida.'.format(imc))
