'''
crie uma tupla q totalmente preenchida com uma contagem por extenso de zero a vinte.
seu programa deve ler um n° pelo teclado entre 1 e 20 e mostra-lo por extenso
'''

cont = ('zero' ,'um', 'dois', 'tres', 'quatro', 'cinco',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
        'treze', 'quatorze', 'quinze', 'dezeseis',
        'dezesete', 'dezoito', 'dezemove', 'vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print(' tente novamente ', end='')

print(f'Vc digitou o numero {cont[num]}')

