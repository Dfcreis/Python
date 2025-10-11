
n = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
soma = n+ n2
print('A soma dos valores {} e {} e igual a {}'.format(n, n2 ,soma))
n3 = input('Digite alguma coisa: ')
print(type(n3))
print('{} e um numero? {}'.format(n3, n3.isnumeric()))
print('{} e um texto? {}'.format(n3, n3.isalpha()))
print('{} e um alpha numerico? {}'.format(n3, n3.isalnum()))
print('{} esta tudo em maiusculo? {}'.format(n3, n3.isupper()))
print('{} esta tudo em minusculo? {}'.format(n3, n3.islower()))