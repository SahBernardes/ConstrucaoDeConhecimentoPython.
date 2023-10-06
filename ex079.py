'''
Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente.
'''

num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('adicionado com sucesso!')
    else:
        print('valor duplicado! não vou cadastrar')

    r = str(input('Quer continuar? [s/n] '))
    if r in 'Nn':
        break
print('-=' * 30)
num.sort()
print(f'vc digitou os valores {num}')
