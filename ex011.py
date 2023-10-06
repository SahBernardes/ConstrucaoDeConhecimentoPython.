#Faça um programa q leia a largura e a altura de uma parede em metros , calcule sua área e a
#quantidade de tinta necessaria para pinta-la, sabendo q para cada litro de tinta pinta uma
#área de 2m cubicos

a = float(input('Altura da parede? '))
l = float(input('largura da parede? '))
area = a * l
tinta = area / 2
print('\033[30;44m Sua parede tem {}X{} de dimenção, \033[m\n'
      '\033[30;43m e sua área de {}m² \033[m\n'
      '\033[30;42m para pinta-la, vai precisar de {}l de tinta.\033[m'.format(a, l, area, tinta))