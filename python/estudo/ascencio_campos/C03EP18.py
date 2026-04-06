"""
Faça um programa que receba uma temperatura em Celsius, calcule e mostre
essa temperatura em Fahrenheit.

"""
temp_celcius = float(input('Insira o valor da temperatura em Celsius: '))

temp_fahrenheit = (temp_celcius * (9/5)) + 32

print(f'{temp_celcius:.2f}°C corresponde a {temp_fahrenheit:.2f}°F')
