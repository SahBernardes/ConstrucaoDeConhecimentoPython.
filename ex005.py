# faça um programa q leia um numero inteiro e mostre na tela seu antecessor e seu sucesor

n = int(input('digite um valor'))
a = n - 1
s = n + 1

print('O antecessor de {}{}{}é {}{}{}e o sucessor é {}{}{}'.format('\033[1;33m', n, ' \033[m',
                                                                     '\033[1;33m', a, ' \033[m',
                                                                     '\033[1;33m', s, ' \033[m'))
