'''
crie um programa q faça o pc jogar jokenpo (pedra parel tesoura -largato spok-)
'''

from random import  randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogador = int(input('Qual é a sua jogada?'))

print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po!!!')
sleep(1)

print('-=' * 15)
print('O computador escolheu {}'.format(itens[pc]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=' * 15)

if pc == 0: #pedra
    if jogador == 0:
        print('Empatou!')
    elif jogador == 1:
        print('Jogador Venceu!')
    elif jogador == 2:
        print('Pc Venceu!')

elif pc == 1: #papel
    if jogador == 0:
        print('Pc Venceu!')
    elif jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('Jogador Venceu!')

elif pc == 2: #tesoura
    if jogador == 0:
        print('Jogador Venceu!')
    elif jogador == 1:
        print('Pc Venceu!')
    elif jogador == 2:
        print('Empatou!')

else:
    print('Jogada Invalida!')

print('-=' * 15)

