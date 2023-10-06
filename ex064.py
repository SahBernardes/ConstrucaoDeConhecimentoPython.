'''
crie um prog q leia varios n°s inteiros pelo teclado, o prog só vai parar quando o usuario digitar o valor 999, q é
a condição de parada. no final mostre quantos n°s foram digitados e qual foi a soma entre eles (desconsoderando o flag
- 999 - )
'''
#minha solução:
'''
n = 0
c = 0
s = 0
while n != 999:
    n = int(input('Digite um valor: '))
    s += n
    c += 1

print(''
Foram digitados {} números
A soma entre eles é de {}
''.format(c - 1, s - 999))
'''
#solução aula:

num = 0
cont = 0
soma = 0
num = int(input('Digite um numero (999 p. parar): '))
while num != 999:
     soma += num
     cont += 1
     num = int(input('Digite um numero (999 p. parar): '))
print(' Você digitou {} números e a soma deles foi {}'.format(cont, soma))