'''Calculando Hipotenusa'''
from math import hypot
print('Vamos calcular o valor da Hipotenusa de um triangulo retangulo')
a = int(input('Me fale o valor do primeiro cateto? '))
b = int(input('Me fale o valor do segundo cateto? '))
c = hypot(a, b)
print('A soma hipotenusa dos catetors {} e {} e igual a {}'.format(a, b ,c))