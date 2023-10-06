'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols
feitos durante o campeonato.
'''

jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do Jogador:'))
tot = int(input('Quantas partidas jogou? '))
for c in range(1, tot + 1):
    partidas.append(int(input(f'- Quantos gols na partida {c}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('*' * 50)
print(jogador)
print('*' * 50)
for k, v in jogador.items():
    print(f'{k} = {v}')
print('*' * 50)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} particas')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i + 1}, fez {v} gols')
print(f'aproveitamento de {jogador["total"]} gols')
print('*' * 50)
