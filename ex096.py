'''
Faça um programa que tenha uma função chamada área(), que receba as
dimensões de um terreno retangular (largura e comprimento) e mostre
a área do terreno.
'''


def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {a}m².')


# programaPrincipal
print('Controle de Terrenos:')
l = float(input('Largura(m): '))
c = float(input('Comprimento: '))
area(l, c)