'''
 Faça um programa que tenha uma função chamada maior(),
 que receba vários parâmetros com valores inteiros.
 Seu programa tem que analisar todos os valores e dizer
 qual deles é o maior.
'''
from time import sleep


def s():
    print('*' * 50)


def maior(* num):
    co = maior = 0
    s()
    print('Analizando os valores...')
    s()
    for v in num:
        print(f'{v} ', end='', flush=True)
        sleep(0.2)
        if co == 0:
            maior = v
        elif v > maior:
            maior = v
        co +=1
    print(f'\nForam informados {co} valoes e o maior valor é {v}!')





# programaP
maior(2, 8, 6, 9, 20, 7)

maior(4, 9, 1)

maior(25, 12)

maior(6)

maior(0)
