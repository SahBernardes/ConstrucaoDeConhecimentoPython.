'''
Desenvolva um programa que leia quatro valores pelo
teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares
'''

n = ( int(input('Digite um número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite o ultimo número: ')))
print(f'vc digitos os numeros {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'o valor 3 apareceu na {n.index(3)+1}° posição')
else:
    print('valor 3 não digitado')
print(f'os valores pares foram : ', end='')
for p in n:
    if p % 2 == 0:
        print(p, end=' ')
