# Conversor de temperatura

TC = float(input('Digite a temperatura em ºC: '))

TK = TC + 273.15
TF = (9 * TC / 5) + 32

print('{:.2F}ºC equivale a {:.2F}ºF e {:.2F}K'.format(TC, TF, TK))
