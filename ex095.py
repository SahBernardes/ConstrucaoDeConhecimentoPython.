'''
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador.
'''
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador:'))
    tot = int(input('Quantas partidas jogou? '))
    partidas.clear()
    for c in range(1, tot + 1):
        partidas.append(int(input(f'- Quantos gols na partida {c}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        res = str(input('Quer continuar? [S|N] ')).upper()[0]
        if res in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if res == 'N':
        break

print('*' * 50)
for i in jogador.keys():
    print(f'{i:<17}', end=' ')
print()
print('*' * 50)
for k, v in enumerate(time):
    print(f'{k + 1:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('*' * 50)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca>= len(time):
        print(f'Erro! Não existe jogador com code {busca}')
    else:
        print(f'Levantamento do jogador {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i + 1} fez {g} gols')
print('*' * 50)
print('Volte Sempre!!!')