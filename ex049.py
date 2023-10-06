'''
refaça o desafio 9, mostrando a tabuada de um n° q o usuario escolher, agr utilizando 'for'
'''
#minha solução:
num = int(input('Digite um numero inteiro: '))
for n in range(1, 11):
    m = num * n
    print('{} x {} = {}'.format(num, n, m))

#solução aula:
nu = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(nu, c, nu * c))
