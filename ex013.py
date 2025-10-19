'''Sorteio de Nomes'''
from random import choice
n1 = input('Digite o nome da primeira pessoa')
n2 = input('Digite o nome da segunda pessoa')
n3 = input('Digite o nome da terceira pessoa')
n4 = input('Digite o nome da quarta pessoa')
nomes = [n1, n2, n3, n4]
escolhidos = choice(nomes)
print('O sorteado foi {}'.format(escolhidos))