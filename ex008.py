largura = float(input('Me fale a largura da parede: '))
altura = float(input( 'Me fale a altura da parede: '))
area = altura * largura
print('Sua parede tem a dimenção de {} x {} e a sua area é de {}m²'.format(largura, altura, area))
tinta = area / 2
print('para pintar esta parede, você ira precisar de {}L de tinta'.format(tinta))