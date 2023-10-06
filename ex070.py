'''
crie um programa que leia o nome e o peço de varios produtos. O programa deveá perguntar se o usuario vai continuar ou
não. No final mostre
a- qual é o total gasto na compra
b- quantos produtos custam mais de R$ 1.000
c- qual produto mais barato
'''
''' #minha solução (no barato ainda n deu bom)
c = 0
total = 0
caro = 0
barato = 0

while True:
    produ = str(input('Nome do produto: '))
    preco = float(input('Preço do Produto: '))
    if preco >= 1000:
        caro += 1

    c +=1
    cad = ' '
    cad = str(input('Deseja continuar cadastrando? [S/N]')).strip().upper()[0]
    while cad not in 'SN':
        cad = str(input('Opção Invalida, Deseja continuar cadastrando? [S/N]')).strip().upper()[0]
    if cad == 'S':
        print('Novo cadastro')
    elif cad == 'N':
        break

    total += preco

print(f''A compra custou R${total}
{caro} produto(s) custaram + de R$ 1.000
{barato} foi o produto mais barato'')
''' #solução aula:

total = totMil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totMil +=1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
#se o prox produto e mais barato q o primeiro, então o menor passa a contar, assim sucessivamente verificado
#e o barato recebe o nome do produto q custa menos

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quetr continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total da compra foi R${total:.2f}')
print(f'{totMil} custaram mais de 1.000 reais')
print(f'O produto mais barato foi {barato} q custa R${menor:.2}')