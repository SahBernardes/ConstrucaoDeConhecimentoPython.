'''
refaça o desafio 51, lendo o 1° termo e a razão de uma PA, mostrando os 10 primeiros termos da progreção usando
a estrutura while
'''

print('Gerador de PA')
print('-='*10)
pri = int(input('Primeiro termo: '))
ra = int(input('Razão da PA: '))
termo = pri
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += ra
    cont += 1
print('Fim')
