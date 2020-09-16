# VERSÃO 2.

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))

ordem = sorted([v1, v2, v3])
menor, meio, maior = ordem[0], ordem[1], ordem[2]

if maior < menor + meio:
    print('Pode formar um triângulo', end=' ') 
    if menor == meio == maior: 
        print('equilátero.')
    elif maior == meio or maior == menor or meio == menor:
        print('isósceles.')
    else: print('escaleno.')
else:
    print('Não pode formar um triângulo.')