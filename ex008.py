#faça um programa que leia o valor em metros e o exiba convertido em centimetros e milimitros

mt = float(input('Quantos metros? '))
cm = mt * 100
mm = mt * 1000

print('\033[4;40m {} metros \033[m \n\033[4;40m são {:>2} centimetros \033[m\n\033[4;40m e {:>2} milimetros \033[m'.format(mt, cm, mm))