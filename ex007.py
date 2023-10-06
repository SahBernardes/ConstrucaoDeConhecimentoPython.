#desenvolva um programa q leia as 2 notas de um aluno, calcule e mostre sua media

nome= str(input('\033[33m Nome do aluno: '))
nota1= float(input('Digite a primeira nota: '))
nota2= float(input('Digite a segunda nota: \033[m'))
media= (nota1 + nota2) / 2

print('A media do aluno {}{}{} e de {}{:.1f}{}'.format('\033[1;36m', nome, '\033[m', '\033[1;34m', media, '\033[m'))