#faça um programa que leia algo no teclado e mostre na tela seus tipos primitivos#
#e todas as informações possiveis sobre ele#

a = input('\033[1;31m digite alguma coisa: \033[m')
print('\033[30;41m O tipo primitovo desse valor é ', type(a), '  \033[m')
print('\033[30;41m Só tem espaços? ', a.isspace(), '                         \033[m')
print('\033[30;41m Tem apenas letras? ', a.isalpha(), '                       \033[m')
print('\033[30;41m Tem apenas letras maiusculas?', a.isupper(), '            \033[m')
print('\033[30;41m Tem apenas letras minusculas? ', a.islower(),'            \033[m')
print('\033[30;41m E alfanumerico?', a.isalnum(), '                           \033[m')
print('\033[30;41m E apenas numerico?', a.isnumeric(), '                       \033[m')
print('\033[30;41m Tem decimal? ', a.isdecimal(), '                            \033[m')
print('\033[30;41m são digitos? ', a.isdigit(), '                            \033[m')
print('\033[30;41m É um titulo?', a.istitle(), '                             \033[m')