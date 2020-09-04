# PROGRAMA QUE LEIA O NOME DE CINCO ALUNOS E SORTEIE A ORDEM DE 
# APRESENTAÇÃO ENTRE ELES.

import random
print('===== ORDEM DE APRESENTAÇÃO =====')
p1 = str(input('Digite o nome da primeira pessoa: '))
p2 = str(input('Digite o nome da segunda pessoa: '))
p3 = str(input('Digite o nome da terceira pessoa: '))
p4 = str(input('Digite o nome da quarta pessoa: '))
p5 = str(input('Digite o nome da quinta pessoa: '))
a = [p1, p2, p3, p4, p5]
random.shuffle(a)
print('A ordem de apresentação ficou: ',end='')
print(a)
