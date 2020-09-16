import random

v1 = str(input('Digite o nome do primeiro item: '))
v2 = str(input('Digite o nome do segundo item: '))
v3 = str(input('Digite o nome do terceiro item: '))
lista = [v1, v2, v3]
s = random.choice(lista)

print(f'O item sorteado foi: {s}.\n')