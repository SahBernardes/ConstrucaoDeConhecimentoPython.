'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] =int(input(f'Digiteum valor para [{l}, {c}]: '))
print('*' * 35)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'|{matriz[l][c]:^5}|', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('*' * 35)
print(f'a soma dos valores pares é de: {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'a soma da 3° coluna é: {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'o maior valor da 2° linha é {mai}.')

