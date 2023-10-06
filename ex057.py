'''
 Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
 peça a digitação novamente até ter um valor correto.
'''

s = str(input('Informe seu sexo? [F/M]')).strip().upper()[0]
while s not in 'MmFf':
     s = str(input('Dados invalido! \nPor favor informe, Qual seu sexo? [F/M]')).strip().upper()[0]
print('Cadastro efetuado com sucesso!')
