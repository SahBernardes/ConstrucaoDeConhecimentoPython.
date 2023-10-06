'''
 Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, crie duas listas extras que vão conter apenas os valores
 pares e os valores ímpares digitados, respectivamente. Ao final, mostre
 o conteúdo das três listas geradas.
'''

lista = []
listaI =[]
listaP = []

while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [s/n] '))
    if r in 'Nn':
        break
for i, n in enumerate(lista):
    if n % 2 == 0:
        listaP.append(n)
    elif n % 2 == 1:
        listaI.append(n)

print('-='*30)
print(f'vc digitou {lista}. \nos numeros {listaI} são impares e os {listaP} são pares')
