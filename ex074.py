'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma
tupla. Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
'''
from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'os valores sortiados foram: {n}')
print(f'o menir valor foi: {max(n)} ')
print(f'o maior valor foi: {min(n)}')