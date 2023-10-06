#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de
# trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.
from random import shuffle
n1 = str(input('\033[1mNome do aluno: '))
n2 = str(input('Nome do aluno: '))
n3 = str(input('Nome do aluno: '))
n4 = str(input('Nome do aluno: \033[m'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('\033[1;30;041mA ordem de apresentação será: ')
print(lista)


