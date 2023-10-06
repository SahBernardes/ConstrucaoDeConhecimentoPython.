'''
 Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu
programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep


def s():
    print('*' * 40)


def contador(i, f, p):
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}:')

    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += p
        print('Fim!')
    else:
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= p
        print('Fim!')


# ProgramaP
s()
contador(1, 10, 1)
s()
contador(10, 0, 2)
s()
print('Personalize a Contagem:')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
s()
contador(ini, fim, pas)
s()
