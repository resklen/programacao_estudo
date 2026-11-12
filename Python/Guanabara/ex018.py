from math import radians, sin, cos, tan
ang = float(input('Digite o valor do ângulo em grau: '))

ang_rad = radians(ang)
seno = sin(ang_rad)
coss = cos(ang_rad)
tg = tan(ang_rad)

print('{:.0f}º corresponde a {:.2f} radianos'.format(ang, ang_rad))
print('O seno de {:.0f}º é {:.2f}'.format(ang, seno))
print('O cosseno de {:.0f}º é {:.2f}'.format(ang, coss))
print('A tangente de {:.0f}º é {:.2f}'.format(ang, tg))
