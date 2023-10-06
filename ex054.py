'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.
'''
#minha solução:
from datetime import date
atual = date.today().year
cma = 0
cme = 0
for c in range(0, 7):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    idd = atual - ano
    if idd >= 21:
        cma += 1
    elif idd < 21:
        cme += 1
print('Das 7 pessoas {} atingiram a sua maioridade e {} ainda são menores de idade'.format(cma, cme))

#solução aula:
#parecido
