'''
 Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint
v = 0
while True:
    print('*' * 25)
    j = int(input('Diga um valor: '))
    pc = randint(0, 10)
    total = j + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Impar ou Par? [I/P] ')).strip().upper()[0]
    print('*' * 15)
    print(f'vc jogou {j} e o computador {pc}. total de {total}', end='')
    print(' Deu Par' if total %2 ==0 else ' Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Vc venceu!')
            v += 1
        else:
            print('Vc Perdeu!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Vc Venceu!')
            v += 1
        else:
            print('Vc perdeu')
            break
    print('*' * 25)
    print('Vamos Jogar Novamente...')
print(f'Vc Venceu {v} Vezes!')
print('*' * 25)



