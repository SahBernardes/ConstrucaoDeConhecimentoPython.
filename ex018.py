#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
# seno, cosseno e tangente desse ângulo.

import math
an = float(input('Digite o amgulo que vc deseja: '))
seno = math.sin(math.radians(an))
cose = math.cos(math.radians(an))
tang = math.tan(math.radians(an))
print('O ângulo de {}{}{} \nTem o seno de {}{:.2f}{} \nTem o cosseno de {}{:.2f}{}\nE a tangente de {}{:.2f}{} '.format('\033[33m', an,'\033[m',
                                                                                                                        '\033[33m', seno,'\033[m',
                                                                                                                        '\033[33m', cose, '\033[m',
                                                                                                                        '\033[33m', tang, '\033[m'))
