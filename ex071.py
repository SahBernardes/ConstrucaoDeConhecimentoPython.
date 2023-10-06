'''
Crie um programa que simule o funcionamento de um caixa eletronico. No início, pergunte ao usuario qual será o valor a
ser sacado (int) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50; R$20; R$10 e R$1
'''

print('*' * 40)
print('{:^40}'.format('Banco'))
print('*' * 40)
valor = int(input('Quanto vc quer sacar? R$'))
total = valor
cedula = 50
totCedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totCedula += 1
    else:
        if totCedula > 0:
            print(f'Total de {totCedula} e de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totCedula = 0
        if total == 0:
            break
print('*' * 40)
print('{:^40}'.format('Volte Sempre'))
print('*' * 40)

