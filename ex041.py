'''
a confederação nacional de natação precisa de um programa q leia o ano de nascimento de um atleta e
mostre sua categoria, de acordo com a idd:
ate 9 anos = mirim
ate 14 anos = infantil
ate 19 anos = junior
ate 25 anos = senior
acima = master
'''
#minha solução:
'''idd = int(input('Digite sua idade: '))

if idd <= 9:
    print('Nadador Mirim')
elif idd > 9 and idd <= 14:
    print('Nadador Infantil')
elif idd > 14 and idd <= 19:
    print('Nadador Junior')
elif idd == 20:
    print('Nadador Senior')
else:
    print('Nadador Master')'''

#solução aula:
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idd = atual - nasc
print('O atleta tem {} anos'.format(idd))
if idd <= 9:
    print('Nadador Mirim')
elif idd <= 14:
    print('Nadador Infantil')
elif idd <= 19:
    print('Nadador Junior')
elif idd <= 25:
    print('Nadador Senior')
else:
    print('Nadador Master')



