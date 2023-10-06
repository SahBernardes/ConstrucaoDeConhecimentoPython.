'''Crie um programa q leia o nome de uma pessoa e diga se tem 'Silva' no nome . '''

'''nome = str(input('Nome completo: ')).strip()
n = nome.upper()
tem = 'SILVA' in n
print('O nome tem Silva? {}'.format(tem))'''

#solução aula

nome = str(input('\033[1;30mNome Completo: ')).strip()
print('O nome tem Silva? {}\033[m'.format('silva' in nome.lower()))
