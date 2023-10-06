#Faça um algoritmo q leia o salario de um funcionario e mostre seu novo valor, com 15% de almento

f= str(input('nome do funcionario: '))
s1 = float(input('digite seu salario: R$'))
al = s1 + (s1 * 15 / 100)


print('Com \033[31m15%\033[m de almento a/o funcionaria(o) {}  q ganhava \033[35m{}\033[m passara a receber deo salario de R$\033[34m{:.2f}\033[m.'.format(f, s1, al))