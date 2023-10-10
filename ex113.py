'''
 113: Reescreva a função leiaInt() que fizemos no desafio 104,
 incluindo agora a possibilidade da digitação de um número de
 tipo inválido. Aproveite e crie também uma função leiaFloat()
 com a mesma funcionalidade.
'''


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um n° inteiro valido: \033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo Usuario. \033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO¹ Digite um n° real valido: \033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuario. \033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um n° inteiro: ')
n2 = leiaFloat('Digite um n° real: ')

print(f'Vc digitou {n1} como Inteiro e {n2} para o valor real')
