'''
Faça um programa q leia 3 numeros e mostre qual é o maior e qual e o menor
'''

n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite mais um numero inteiro: '))
n3 = int(input('Digite mais um numero inteiro: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print('O menor valor digitado foi {}{}{}'.format('\033[36m', menor, '\033[m'))

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n2 and n3 > n1:
    maior = n3
print('O maior valor foi {}{}{}'.format('\033[34m',maior, '\033[m'))
