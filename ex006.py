#Crie um algoritimo q leia o numero e mostre seu dobro, triplo e raiz quadrada

n= float(input('digite um valor: '))
d= n * 2
t= n * 3
r= n ** (1/2)

print('\033[1;33m O valor digitado é {}, \n'
      ' Seu dobro é {}, \n'
      ' Seu triplo é {} \n '
      'E sua raiz quadrada é {:.2f}'.format(n, d, t, r))