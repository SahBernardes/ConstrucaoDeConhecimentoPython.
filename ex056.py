'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo,
        qual é o nome do homem mais velho
        quantas mulheres têm menos de 20 anos.


'''

sIdd = 0
mIdd = 0
mIddH = 0
nomeHVelho = ''
totM20 = 0

for p in range(1, 5):
    print('-' * 5, '{}° Pessoa'.format(p), '-' * 5)
    nome = str(input('Nome: '))
    idd = int(input('Idade: '))
    sexo = str(input('Sexo [f/m]: ')).strip()
    sIdd += idd
    if p == 1 and sexo in 'Mm':
        mIddH = idd
        nomeHVelho = nome
    if sexo in 'Mm' and idd > mIddH:
        mIddH = idd
        nomeHVelho = nome
    if sexo in 'Ff' and idd < 20:
        totM20 += 1

mIdd = sIdd / 4

print('''a media de idade do gp é {:.0f}. 
O homem mais velho é {} . 
E {} mulheres tem menos de 21 anos.'''.format(mIdd, nomeHVelho, totM20))
