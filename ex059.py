'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

opcao = 0
v1 = int(input('Digite o 1° valor:'))
v2 = int(input('Digite o 2° valor: '))
while opcao != 5:
    print('-*' * 15)
    print('''    [ 1 ] Somar valores
    [ 2 ] Multiplicar valores
    [ 3 ] Maior valor
    [ 4 ] Novos valores
    [ 5 ] Sair do programa''')
    print('-*' * 15)
    opcao = int(input('Escolha uma opção: '))
    print('-*' * 15)
    if opcao == 1:
        print('{} + {} = {}'.format(v1, v2, v1 + v2))
    elif opcao == 2:
        print('{} x {} = {}'.format(v1, v2, v1 * v2))
    elif opcao == 3:
        if v1 > v2:
            print('O maior valor é {}'.format(v1))
        elif v2 > v1:
            print('O maior valor é {}'.format(v2))
        else:
            print('Os números são iguais')
    elif opcao == 4:
        print('Novos Valores:')
        v1 = int(input('Digite o 1° valor:'))
        v2 = int(input('Digite o 2° valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção Invalida')
print('Fim do Programa!')

