#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

'''co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacent: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A Hipotenusa vai medir {:.2f}'.format(hi))'''

from math import hypot
co = float(input('\033[34mComprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacent: '))
hi = hypot(co, ca)
print('A Hipotenusa vai medir\033[m \033[33m{:.2f}'.format(hi))
