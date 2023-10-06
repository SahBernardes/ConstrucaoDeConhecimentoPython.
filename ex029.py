'''
escreva um programa q leia a velociddde um carro e mostre se ele ultrapassar 80km/h, mostre na tela dizendo
q ele foi multado.
A multa vai custar R$ 7,00 por km acima do limite
'''
#minha solução:
km = int(input('\033[1mQuantos Km por Hr?\033[m '))
kmm = (km - 80) * 7

if km > 80:
    print('\033[31mSua multa será de R$: {}\033[m'.format(kmm))
else:
    print('\033[32mSem multa\033[m')
print('\033[1mTenha um bom dia! Dirija com segurança!\033[m')
#solução aula: parecido
