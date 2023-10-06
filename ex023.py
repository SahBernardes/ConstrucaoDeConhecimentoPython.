'''Faça um programa que leia um número de 0 a 9999 e mostre
na tela cada um dos dígitos separados.
'''

n = int(input('Informe o valor: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('\033[32m analisando o numero {}\033[m'.format(n))
print(' \033[7;36m Unidade: {} \033[m\n \033[7;36m Dezena:  {} \033[m\n \033[7;36m Centena: {} \033[m\n \033[7;36m Milhar:  {} \033[m'.format(u, d, c, m))