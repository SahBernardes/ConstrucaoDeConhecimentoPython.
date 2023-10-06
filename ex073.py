'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('corinthians', 'palmeiras', 'santos', 'grêmio',
         'cruzeiro', 'Flamengo', 'vasco', 'chapecoense',
         'atlético', 'Botafogo', 'atlético-PR', 'bahia',
         'são paulo', 'fluminense', 'sport recife',
         'EC vitoria', 'curitiba', 'avaí', 'ponte preta',
         'atletico-GO')
print('*' * 267)
print(f'Lista de times: {times}')
print('*' * 267)
print(f'os 5 primeiros times são: {times[0:5]}')
print('*' * 267)
print(f'os 4 ultioms são: {times [-4:]}')
print('*' * 267)
print(f'em ordem alfabetica: {sorted(times)}')
print('*' * 267)
print(f'o chapecoence esta na {times.index("chapecoense")+1}° colocação')
print('*' * 267)
