'''
Crie um programa que tenha a função leiaInt(), que vai funcionar
de forma semelhante 'a função input() do Python, só que fazendo
a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
'''


def leiaInt(msg):
    ok = False
    v = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            v = int(n)
            ok = True
        else:
            print('\033[0;31mErro! digite um n° inteiro valido: \033[m')
        if ok:
            break
    return v


#prog principal:
n = leiaInt('Digite um n°: ')
print(f'Vc digitou o n° {n}')
