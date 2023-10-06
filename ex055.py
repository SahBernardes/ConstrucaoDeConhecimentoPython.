'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior eo menor peso lidos.
'''

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso de {}° pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso é {}Kg e o menor peso é {}Kg'.format(maior, menor))
