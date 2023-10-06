#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('qual a temperatura? °C'))
f = (( 9 * c ) / 5 ) +32

print('\033[1;30;47m {}°C e igual a {}°F \033[m'.format(c, f))