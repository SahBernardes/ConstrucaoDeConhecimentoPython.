'''faça um programa q leia uma frase e mostre:
 quantas vzs a letra 'a' aparece
 em q posição aparece pela 1° vez
 em q posição aparece pela ultima vez
 '''
#consegui sozinha ate aq

'''frase = str(input('Escreva uma frase: '))
quantosA = frase.count('a')
posi1 = frase.find('a')
#untposi=
print('Na frase : {}.\nTem {} letras a' .format(frase, quantosA))
print('o 1° a esta na posição {} e o ultimo na posição '. format(posi1))'''

#solução aula
frase = str(input('\033[1mEscreva uma frase: \033[m')).upper().strip()
print('\033[35mA letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição {}\033[m'.format(frase.rfind('A')+1))