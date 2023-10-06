'''crie um desafio q leia o nome de uma cidade e diga se ela começa
ou não com o nome 'santos'. '''

#c = str(input('Em que cidade vc nasceu? '))
#tems = 'Santo' in c
#separa = c.split()
#onde = separa[0] == 'Santo' in c
#print('O nome tem Santo? {}'.format(tems))
#print('É o Primeiro nome? {}'.format(onde))

#solução aula
#city = str(input('Em q cidd vc nasceu?')).strip()
#print(city[:5].upper() == 'SANTO')


#junção das soluções

c = str(input('\033[1mEm que cidade vc nasceu? \033[m')).strip()
tem = 'SANTO' in c.upper()
separa = c.split()
onde = separa[0] == 'SANTO'

print('\033[36mO nome tem Santo? {}'.format(tem))
print('É o primeiro nome? {}\033[m'.format(onde))

