#Faça um algoritmo q leiao preço de um produto e mostre seu novo valor com 5% de descosto

presso1 = float(input('qual o presso do produto : R$'))
des = presso1 - (presso1 * 5 / 100)


print('o presso atual do produto é de :\033[31m R${:.2f} \033[m'.format(des))