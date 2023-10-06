'''
 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
ou então o empréstimo será negado.
'''
#minha resposta:
'''nome = str(input('Nome do cliente: '))

casa = float(input('Valor da casa: '))
s = float(input('Salario do cliente: '))
anos = int(input('em quantos anos quer pagar: '))

mensalidade = s + (s * 30 / 100)
meses = anos / 12
tempo = (casa / meses)

if tempo <= mensalidade:
    print('Emprestimo Aprovado!')
elif tempo > mensalidade:
    print('Emprestimo Reprovado!')'''


#resposta aula:
casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo= salario * 30 / 100

print('para pagar uma casa de R${:.2f} em {} anos,'.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Emprestimo consedido')
else:
    print('Emprestimo Negado')

