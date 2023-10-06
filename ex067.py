'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
''' #minha solução:
'''
while True:
    n = int(input('Digite o numero para saber sua Tabuada : '))
    if n <= 0:
        break

    print(f''A tabuada {n} de é: 
        {n} x 1 = {n * 1}
        {n} x 2 = {n * 2}
        {n} x 3 = {n * 3}
        {n} x 4 = {n * 4}
        {n} x 5 = {n * 5}
        {n} x 6 = {n * 6}
        {n} x 7 = {n * 7}
        {n} x 8 = {n * 8}
        {n} x 9 = {n * 9}
        {n} x 10 = {n * 10}'')
print('Programa de tabuada encerrado, Volte Sempre !')
'''
#solução aula

while True:
    n = int(input('Digite o numero para saber sua Tabuada : '))
    print('-' * 25)
    if n <= 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 25)
print('Programa de tabuada encerrado, Volte Sempre !')
