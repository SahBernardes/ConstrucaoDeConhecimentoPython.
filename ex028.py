'''
escreva um programa q faça o pc "pensar" em um numero inteiro entre 1 e 5 e peça para o usuario
tentar descobri q numero foi escolhido.
o programa deve escrever na tea se o usuario venceu ou perdeu
'''
#minha solução:

from random import choice, randint
'''n = int(input('Digite um número de 1 á 5: '))
list = [1, 2, 3, 4, 5]
escolhido = choice(list)
print('o número escolhido pelo programa foi {}'.format(escolhido))
if n == escolhido:
    print('Vc Venceu!')
else:
    print('Vc Perdeu!')'''

#solução da aula:

pc = randint(1,5)
print('\033[35m-=-\033[m'*13)
print('Vou pensar em um numero entre 1 e 5...')
print('\033[35m-=-\033[m' * 13 )
jog = int(input('Em q numero eu pensei? '))
print('\033[35m-=-\033[m' * 13 )
print('Pensei no número... {}'.format(pc))
if jog == pc:
    print('Vc ganhou!')
else:
    print('Vc perdeu!')

print('\033[35m-=-\033[m' * 13)

