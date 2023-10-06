'''
faça um programa q leia o ano de nascimento de um jovem e informe, de acordo com a idd :
se ele vai se alistar ao serviço militar (tbm deve mostrar o quanto falta)
se é hr de se alistar
se ja passou a hr do alistamento (tbm deve mostrar quanto tempo passou do alistamento)
'''
#minha solução:
'''ano = int(input('Digite o ano de seu nascimento: '))
idd = 2020 - ano
falta = 18 - idd
passou = idd - 18
print('Vc tem {} anos'.format(idd))
if idd < 18:
    print('ainda falta {} anos para se apresentar ao alistamento de serviço militar'.format(falta))
elif idd == 18:
    print('E hr de se alistar ao serviço milita')
elif idd > 18:
    print('Já se passou {} anos do seu alistamento militar'.format(passou))
'''

#solução aula:
from datetime import date
atual = date.today().year
nasc = int(input('ano de nascimento: '))
idd = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idd, atual))
if idd == 18:
    print('Vc tem q se alistar Imediatamente!')
elif idd < 18:
    saldo = 18 - idd
    print('Ainda faltam {} anos para o alistamento!'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {} ano'.format(ano))
elif idd > 18:
    saldo = idd - 18
    print('Vc já deveria ter se alistado a {} anos!'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {} ano'.format(ano))

