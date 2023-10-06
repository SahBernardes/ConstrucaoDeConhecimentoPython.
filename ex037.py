'''
escreva um programa q leia um n° inteiro qlq e peça p o usuario
escolher qual será a base de corverção
1 p binario
2 p octal
3 p hexadecimal
'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para converção:
[ 1 ] Converter em Binário
[ 2 ] Converter em Octal
[ 3 ] Converter em Hexadecimal''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} Convertido para Binario é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} Convertido para Octal é igual {}'.format(num, oct(num)[2:]))
elif opcao == 3 :
    print('{} Convertido para Hexacecimal e igual {}'.format(num, hex(num)[2:]))
else:
    print('Opção Invalida')

