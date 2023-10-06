'''
desenvolva um programa q leia o comprimento de 3 retas e diga ao usuario se elas podem ou n
formar um triangulo
'''

r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32m Os Seguimentos Podem Formar um Triangulo\033[m')
else:
    print('\033[31m Os Seguimentos Não Podem Formar Um Triangulo\033[m')
