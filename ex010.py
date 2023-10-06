#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares
#essa pessoa pode comprar

real = float(input('quanto dinheiro vc tem? R$'))
dolar = real / 5.09

print('\033[36m R${} compra U${:.2f} \033[m'.format(real, dolar))