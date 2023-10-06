'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''
#minha solução:
'''pMaior = 0
pmenor = 0
m = 0
f = 0
fmenor = 0
c = 0
while True:
    sexo= str(input('Digite Seu Sexo: ')).strip().upper()[0]
    idade= int(input('Digite Sua Idade: '))
    if idade >= 18:
        pMaior += 1
    elif idade < 18:
        pmenor += 1

    while sexo not in 'FM':
        print('Opção Invalida')
        break
    if sexo == 'F':
        f += 1
        if f and idade < 20:
            fmenor += 1

    elif sexo == 'M':
        m += 1

    c += 1
    cad = ' '
    cad = str(input('Deseja continuar cadastrando? [S/N]')).strip().upper()[0]
    while cad not in 'SN':
        cad = str(input('Opção Invalida, Deseja continuar cadastrando? [S/N]')).strip().upper()[0]
    if cad == 'S':
        print('Novo cadastro')

    elif cad == 'N':
        break

print(f''{c} pessoas foram cadastradas
{pMaior} São maiores de idade
{m} homens foram cadastrados 
{fmenor} mulheres tem menos de 20 anos de idade'')'''

#solução aula:

tot18 = totH = totM20 = 0
while True:
    idade = int(input('idade: '))
    if idade >= 18:
        tot18 +=1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        totH +=1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'pessoas maiores de idade: {tot18}')
print(f'temos {totH} Homens cadastrados')
print(f'{totM20} Mulheres tem menos de 20 anos')
