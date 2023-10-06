'''
 Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

print('Gerador de PA')
print('-=' * 10)
pri = int(input('Primeiro termo: '))
ra = int(input('Razão da PA: '))
termo = pri
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += ra
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos vc quer mostrar a mais? '))
print('Finalizado com {} termos mostrados'.format(total))