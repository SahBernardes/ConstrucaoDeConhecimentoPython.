#Segundo o padrão ANSI:

'''
style -> 0 none         | text -> 30 Preto      <- 40 back |
         1 bold         |      -> 31 vermelho   <- 41      |
         4 underline    |      -> 32 verde      <- 42      |
         7 negative     |      -> 33 amarelo    <- 43      |
                        |      -> 34 azul       <- 44      |
                        |      -> 35 roxo       <- 45      |
                        |      -> 36 azul claro <- 46      |
                        |      -> 37 cinza      <- 47      |

ex.: \033[ style; text; back m
     \033[  0   ; 30  ;  44 m
     \033[m -> Padrão do Terminal
     \033[7;30 -> letra preta e fundo branco (o 7 inverte as cores)
'''

#ex em uso:

print('\033[4;30;45m Olá Mundo \033[m')
print('Olá, Prazer em te conhecer {} Sah {}'.format('\033[4;34m', '\033[m'))
print('\033[0;30;41m Sua cor será vermelho\033[m')
print('\033[33m Da pra usar apenas 1 coisa\033[m')
print('\033[1;45m Duas coisas')
print('\033[30m e se não fechar, a configuração da linha anterior prossegue para as linhas seguntes')
print('mais vc pode fechar no final de td se quiser \033[m')
print('\n\033[1;30;41m Mais vc pode arrumar de varias madeiras \033[m')
print('\033[1;30;41mBasta usar a imaginação e a criatividade \033[m \n\n ')

#e para ficar facil vc tbm pode fazer assim :

cores = {'azul':'\033[30;44m',
         'nulo':'\033[m'}

print('{} Vc tbm pode usar assim {}'.format(cores['azul'], cores['nulo']))

