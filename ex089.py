'''
Crie um programa que leia nome e duas notas de vários alunos e guarde
tudo em uma lista composta. No final, mostre um boletim contendo a média
de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.
'''

ficha = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('nota1: '))
    n2 = float(input('nota1: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    res = str(input('Quer continuar? [s/n] '))
    if res in 'Nn':
        break

print('*' * 30)
print(f'{"N°":<4}{"Nome:":<10}{"Média":>8}')
print('_' * 25)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('*' * 30)
    opc = int(input('Mostrar notas de qual aluno? (99 interrompe):'))
    if opc == 99:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('Volte Sempre')