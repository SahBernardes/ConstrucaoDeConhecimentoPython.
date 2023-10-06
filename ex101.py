'''
Crie um programa que tenha uma função chamada voto() que vai
receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''


def voto(ano=0000):
    from datetime import date
    atual = date.today().year
    idd = atual - ano
    if idd < 16:
        return f'Com {idd}, VOTO NEGADO!'
    elif 16 <= idd < 18 or idd > 65:
        return f'Com {idd}, VOTO OPCIONAL!'
    else:
        return f'Com {idd}, VOTO OBRIGATORIO!'


nasc = int(input('Em que ano vc nasceu? '))
print(voto(nasc))
