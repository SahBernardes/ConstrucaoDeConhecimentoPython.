"""Faça um programa que tenha uma lista chamada números e duas funções 
 chamadas sorteia() e somaPar(). A primeira função vai sortear 5 
 números e vai colocá-los dentro da lista e a segunda função vai 
 mostrar a soma entre todos os valores pares sorteados pela função 
 anterior. """


from random import randint
from time import sleep


def s():
    print('*' * 50)


def sortear(lista):
    print('Sorteando 5 valores:', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f' {n} ', end='', flush=True)
        sleep(0.3)
    print('Pronto!')

s()


def somaP(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
           soma += v
    print(f'Somando os valores pares, temos {soma}!')
    s()

num = list()
sortear(num)
somaP(num)
