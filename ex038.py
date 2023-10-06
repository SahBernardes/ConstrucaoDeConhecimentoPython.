'''
escreva um programa 1 leia 2 n° inteiros, mostrando uma msg na tela:
o 1° maior
o 2° maior
n existe maior, os 2 são iguais
'''

n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2e valor: '))

if n1 > n2 :
    print('O valor {} é o maior'.format(n1))
elif n1 < n2 :
    print('O valor {} é o maior'.format(n2))
else:
    print('não existe maior, os 2 são iguais')
