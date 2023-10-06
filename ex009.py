#Faça um programa q leia um numero inteiro qualquer e mostre sua tabuada

n = int(input('digite um numero inteiro: '))
x1 = n*1
x2 = n*2
x3 = n*3
x4 = n*4
x5 = n*5
x6 = n*6
x7 = n*7
x8 = n*8
x9 = n*9
x10 = n*10

print('\033[1;30;43m''-' * 20 )
print('A tabuada de {} e :\n'
      '{} x 1 = {}\n'
      '{} x 2 = {}\n'
      '{} x 3 = {}\n'
      '{} x 4 = {}\n'
      '{} x 5 = {}\n'
      '{} x 6 = {}\n'
      '{} x 7 = {}\n'
      '{} x 8 = {}\n'
      '{} x 9 = {}\n'
      '{} x 10 = {}\n'.format(n, n, x1, n, x2, n, x3, n, x4, n, x5, n, x6, n, x7, n, x8, n, x9, n, x10))
print('-' * 20 )