'''
Escreva um programa q pergunte o salario de um funcionario e calcule o valor doseu almento.
P salarios acima de 1.250,00, calcule 10% de almento, para salarios inferiores 15% de almento
'''
#minha solução
f = str(input('Nome do funcionário: '))
s = float(input('Sálario do funcionario: '))
al1 = s + (s * 10 / 100)
al2 = s + (s * 15 / 100)
print('O funcionário \033[34m{}\033[m passará a receber: '.format(f))
if s >= 1250.00:
    print('\033[1mCom um almento de 10%\033[m \033[1;32mR$: {}\033[m'.format(al1))
else:
    print('\033[1m Com um almento de 15%\033[m \033[1;32mR$: {}\033[m'.format(al2))

#solução da aula:
'''salario = float(input('Digite o salário: '))
if salario <= 1250.00 :
    novo = salario + (salario * 10 / 100)
else:
   novo = salario + (salario * 15 / 100)
print('Quem ganhava \033[31m{:.2f}\033[m passará a ganhar \033[32m{:.2f}\033[m'.format(salario, novo))'''
