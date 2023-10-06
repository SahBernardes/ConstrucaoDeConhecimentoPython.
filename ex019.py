#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela
# o nome do escolhido.
from random import choice
n1 = str(input('nome do aluno :'))
n2 = str(input('nome do aluno :'))
n3 = str(input('nome do aluno :'))
n4 = str(input('nome do aluno :'))
list = [n1, n2, n3, n4]
escolhido = choice(list)
print('o aluno escolhido é {}'.format(escolhido))

