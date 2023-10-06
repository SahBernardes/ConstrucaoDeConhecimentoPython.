'''
desenvolva um programa q pergunte a distancia de uma viagem em km e calcule o preço da passagem cobrando
R$0,50 por km p. viagens ate 200 km e R$0,45 p viagens mais longas
'''

'''viagem = float(input('Qual a dintancia em km de sua viagem? '))
v1 = viagem * 0.50
v2 = viagem * 0.45

if viagem <= 200 :
    print('A viagem vai custar R$ {}.'.format(v1))
else:
    print('A viagem vai custar RS {}.'.format(v2))'''

#aula simplificado:

viagem = float(input('Qual a dintancia em km de sua viagem? '))
v = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('A viagem vai custar \033[1;32mR$ {:.2f} \033[m'.format(v))

