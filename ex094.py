'''
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

lista = list()
pessoa = dict()
soma = media =0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M|F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idd'] = int(input('Idade: '))
    soma += pessoa['idd']
    lista.append(pessoa.copy())

    while True:
        res = str(input('Quer continuar? [S|N] ')).upper()[0]
        if res in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if res == 'N':
        break

print('*' * 50)
print(f'-> São {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'-> A média de idade é de {media:5.1f} anos')
print(f'-> As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('-> Lista de pessoas com idade acima da media: ', end='')
for p in lista:
    if p['idd'] >= media:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('*' * 50)
print('Encerrado')
