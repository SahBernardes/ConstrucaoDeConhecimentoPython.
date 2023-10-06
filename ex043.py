'''
escreva um programa q leia a altura e o peso de uma pessoa, calcule seu imc e mostre seu stts:
abaixo de 18.5 - abaixo do peso
entre 18.5 e 25 - peso ideal
entre 25 e 30 - obeso
entre 30 e 40 - obesidade morbida
'''

peso = float(input('Qual e seu peso? '))
alt = float(input('Qual é sua altura? '))
imc = peso / (alt ** 2)
print('seu imc é de {:.1f}'.format(imc))

if 18.5 >= imc:
    print('Vc está abaixo do peso!')
elif 18.6 <= imc < 25:
    print('Vc esta no peso ideal!')
elif 25 <= imc < 30:
    print('Vc esta com sobrepeso')
elif 30<= imc <40:
    print('Vc esta com obesidade')
elif imc <= 40:
    print('Vc esta com obesidade morbida, Cuidado!')
