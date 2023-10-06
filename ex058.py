'''
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
#solução final:
from random import randint
pc = randint(0, 10)
vzs = 0
print('Vou pensar em um n° entre 0 e 10, tente adivinhar qual é')
jog = int(input('Em que n° eu pensei? '))
while jog != pc:
    vzs += 1
    if jog < pc:
        print('Mais...', end='')
    else:
        print('Menos...', end='')
    jog = int(input('Tente outra vez!.. '))
print('''Parabens!!! Vc adivinhou!!!
Vc precisou de {} Vezes para adivinhar'''.format(vzs))

#minha solução:
'''
...
jog = int(input('Em que n° eu pensei? '))
while jog != pc:
    vzs += 1
     jog = int(input('Tente outra vez!.. '))
print('Parabens!!! Vc adivinhou!!!
Vc precisou de {} Vezes para adivinhar'.format(vzs))
'''

#solução aula:
'''
....
print('Vou pensar....')
acertou = false
while not acertou:
    jog = int (input('Qual seu palpite?'))
    vzs +=1
    if jg == pc:
        acertou = true
    else:
          if jog < pc:
            print('Mais...', end='')
        else:
            print('Menos...', end='')
         jog = int(input('Tente outra vez!.. '))  
print('Parabens!!! Vc adivinhou!!!
Vc precisou de {} tentativas'.format(vzs))
'''
