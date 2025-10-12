prod = float(input(' Me fale o preço do Produto? R$'))
promo = prod * 5 / 100
final = prod - promo
print('Um produto com o preço de R${} em uma promoção de 5%  vai custar R${:.2f}'.format(prod , final ))
