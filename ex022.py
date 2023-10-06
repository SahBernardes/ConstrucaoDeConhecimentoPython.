'''Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
'''

nome= str(input('\033[33mDigite um Nome Completo: \033[m')).strip()
print('\033[32mAnalisando seu nome...\033[m')
print('\033[34mSeu nome em Maiusculo é: {}'.format(nome.upper()))
print('Seu nome em minuscolo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)- nome.count(' ')))
print('Seu primeiro nome tem {} letras\033[m'.format(nome.find(' ')))
#ou
'''separa = nome.strip()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
'''