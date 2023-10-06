'''
refaça o ex35 dos triangulos e mostre q tipo de triangulo sera formado:
equilatero - tds os ldas iguais
isosceles - 2 lds iguais
escaleno - tds os lados diferentes
'''
#minha solução
r1 = float(input('1° seguimento: '))
r2 = float(input('2° seguimento: '))
r3 = float(input('3° seguimento: '))
'''
tri = r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2
eq = r1 == r2 == r3
iso =  r1 == r2 or r1 == r3 or r2 == r3
es = r1 != r2 != r3 != r1

if tri and eq:
    print('Os Seguimentos Podem Formar um Triangulo do tipo: Equilatero')
elif tri and iso:
    print('Os Seguimentos Podem Formar um Triangulo do tipo: Isosceles')
elif tri and es:
    print('Os Seguimentos Podem Formar um Triangulo do tipo: Escaleno')
else:
    print('Os Seguimentos Não Podem Formar Um Triangulo')
'''

#solução aula:
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Seguimentos Podem Formar um Triangulo ',end='')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('Os Seguimentos Não Podem Formar Um Triangulo')
