'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
while True:
    n = lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [s/n] '))
    if r in 'Nn':
        break

print('-=' * 30)
lista.sort(reverse=True)
print(f'vc digitou {len(lista)} valores')
print(f'os valores em ordem decrescente são {lista}')

if 5 in lista:
    print('O numero 5 esta na lista!')
else:
    print('O numero 5 não esta na lista')



