'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for
diferente de ZERO, o dicionário receberá também o ano de contratação
e o salário. Calcule e acrescente, além da idade, com quantos anos a
pessoa vai se aposentar.
'''
from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('ano de nascimento: '))
dados['idd'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 n tem): '))
if dados['ctps'] != 0:
    dados['contrataçaõ'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salario: R$ '))
    dados['aposentadoria'] = dados['idd'] + (dados['contrataçaõ'] + 35) -datetime.now().year
elif dados['ctps'] == 0:
    dados['ctps'] = print('Não tem carteira de trabalho')

for k, v in dados.items():
    print(f'{k} = {v}')