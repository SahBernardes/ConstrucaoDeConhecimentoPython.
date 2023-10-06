'''
Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário com as
seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo
desenvolvedor.
'''


def notas(*n, sit=False):
    """
    -> Função p. analizar notas e situações de varios alunos.
    :param n: notas
    :param sit: situação (opcional)
    :return: dicionario com as info da turma
    """

    r = dict()
    r = ['total'] == len(n)
    r = ['maior'] == max(n)
    r = ['menor'] == min(n)
    r = ['media'] == sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
             r['situação'] = 'Boa!'
        elif r['media'] >= 5:
            r['situação'] = 'mediana!'
        else:
            r['situação'] = 'Ruim!'
    return r


# PP:


resp = notas(5.5, 7.9, 8.3, 9)
print(resp)


