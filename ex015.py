# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('por quantos dias o carro foi alugado? '))
km = float(input('Por quantos km rodados? '))
#dias = d * 60
#kmr = km * 0.15
#aluguel = dias + kmr
# OU
aluguel = (d * 60) + (km * 0.15)
print('vc pagará de aluguel \033[31mR${:.2f}'.format(aluguel))
