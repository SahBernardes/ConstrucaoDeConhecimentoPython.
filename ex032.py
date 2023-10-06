'''
faça um programa q leia um ano qlq e mostre se ele é bisexto
'''
from datetime import date
ano = int(input('Que ano quer analizar? \n Coloque 0 se quizer analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[1m O ano {} é Bisexto\033[m'.format(ano))
else:
    print('\033[1;30m O ano {} não é Bisexto\033[m'.format(ano))
