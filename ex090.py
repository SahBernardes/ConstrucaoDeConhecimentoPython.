'''
 Faça um programa que leia nome e média de um aluno, guardando também
a situação em um dicionário. No final, mostre o conteúdo da estrutura
na tela.
(no exercicio ta pedindo so a media, mais eu quero fazer com que o
proprio programa tire a media a partir das notas)
'''

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
n1 = float(input('1° nota: '))
n2 = float(input('2° nota: '))
n3 = float(input('2° nota: '))
n4 = float(input('2° nota: '))
aluno['media'] = (n1 + n2 + n3 + n4) / 4

if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
elif  5<=  aluno['media'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'

for k, v in aluno.items():
    print(f'{k} = {v}')

