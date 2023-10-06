'''
crie um programa q leia 2 notas de um aluno, mostrando no final de acordo com a media atingida:
abaixo de 5.0 - reprovado
entre 5.0 e 6.9 - recuperação
acima de 6.0- aprovado
'''

aluno = str(input('Nome do aluno: '))
n1 = float(input('1° nota: '))
n2 = float(input('2° nota: '))
media = (n1 + n2) / 2

print('A média do aluno {} foi de {}'.format(aluno, media))
if media < 5:
    print('Aluno Reprovado')
elif 6.9 > media >=5:
    print('Aluno em Recuperação')
elif media >= 7:
    print('Aluno Aprovado')
