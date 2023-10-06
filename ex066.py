'''
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999
(mais eu quis trocar pra 0 "pq sim!" kk),
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
(desconsiderando o flag).
'''

s = c = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 0:
        break
    s += n
    c += 1
print(f'Vc digitou {c} valores. Sua soma é {s}.')
