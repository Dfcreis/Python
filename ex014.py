'''Calculando seno, cos, tan de  um determinado angulo'''
from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo que deseja? '))
seno = sin(radians(angulo))
print('o angulode {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))