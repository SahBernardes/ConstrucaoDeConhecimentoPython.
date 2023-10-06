'''
escreva um programa q calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição
de pagamento:
a vista 10% - desconto
cartão 5 % - desconto
2x no cartao - preço normal
3x ou + no cratão - 20% dejuros
'''
#minha solução:
'''pre = float(input('Qual o preço do produto? '))
pag = str(input('Qual a forma de pagamento? ')).strip().lower()

aVis = pre - (pre * 10 / 100)
car1x = pre - (pre * 5 / 100)
car3x = pre + (pre * 20 / 100)

if pag == 'a vista' :
    print('o valor do produto é R${} com o desconto de 10% custará R${}'.format(pre, aVis))
elif pag == 'debito':
    print('O valor do produto é R${} com o desconto de 5% custará R${}'.format(pre, car1x))
elif pag == 'credito':
    print('O valor do produto é R${} com 20% de juros custará R${}'.format(pre, car3x))
else:
    print('O produto custará R${}'.format(pre))
'''

#solução aula:
preco = float(input('Qual o valor das compras? R$'))
print('''
Formas De Pagamento:
[ 1 ] Á vista dinheiro/cheque
[ 2 ] Á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
opcoes = int(input('Qual é a opção?'))

if opcoes == 1:
    total = preco - (preco * 10 / 100)
elif opcoes == 2:
    total = preco - (preco * 5 / 100)
elif opcoes == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} Sem juros'.format(parcela))
elif opcoes == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totparc, parcela))
else:
    total = preco
    print('Opção de pagamento invalida')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
