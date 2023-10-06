'''
crie um programa q leia um numero inteiro e diga se ele é impar ou par
'''

n = int(input('Digite um número inteiro: '))
if n % 2 == 0:
    print('\033[33m O número é par \033[m')
else:
    print('\033[31m O número é ímpar \033[m')