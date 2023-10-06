'''
crie um prog q leia varios n°s inteiros pelo teclado, no final da execução, mostre a media entre tds os valores
e qual foi o maior e menor valores lidos. o programa deve perguntar ao usuario se ele quer ou não continuar a
digitar valores
'''
# minha solução:
'''
n = 1
c = 0
s = 0
opcao = ''
while opcao != 'N':
    n = int(input('Digite um valor: '))
    c += 1
    s += n
    media = s / c
    opcao = str(input('Deseja continuar? [S/N] ').strip().upper())
print('Vc digitou {} valores e a media deles é de {:.0f}.'.format(c, media))
print('Fim do Programa')
'''
#solução aula

R = 's'
soma = quant = media = maior = menor = 0
while R in 'Ss':
    n = int(input("Digite um numero: "))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    R = str(input('Quer continuar (S/N)? ')).upper().strip()[0]
media = soma / quant
print('''
Vc digitou {} numeros e a média é {} o maior {} e o menor {}
'''.format( quant, media, maior, menor))
