'''
Faça um programa q leia o nome completo de uma pessoa mostrando em seguida o 1° e o ultimo nome separadamente
'''
nome = str(input('\033[1mNome Completo: \033[m')).split()
print('\033[1;30mSeu 1° nome é: {}'.format(nome[0]))
print('Seu Ultimo Nome é: {}\033[m'.format(nome[len(nome)-1]))
