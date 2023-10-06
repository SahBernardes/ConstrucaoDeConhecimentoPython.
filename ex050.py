'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
'''
#minha solução:
s = 0
for c in range(0, 6):
    c = int(input('Digite o {} valor: '.format(c)))
    if c % 2 == 0:
        s += c
print('a soma dos pares e de {}'.format(s))

#solução aula:
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Vc informou {} números pares e a soma foi{}'.format(cont, soma))
