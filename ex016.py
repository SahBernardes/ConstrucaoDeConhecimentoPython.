#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porçaõ inteira é {}'.format(num,trunc(num)))'''

num = float(input('Digite um valor: '))
print('\033[1;30;44m O valor digitado foi {} e sua porçaõ inteira é {} \033[m'.format(num ,int(num) ))
