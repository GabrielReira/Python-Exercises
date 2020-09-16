import random

p1 = str(input('Digite o nome da primeira pessoa: '))
p2 = str(input('Digite o nome da segunda pessoa: '))
p3 = str(input('Digite o nome da terceira pessoa: '))
p4 = str(input('Digite o nome da quarta pessoa: '))
p5 = str(input('Digite o nome da quinta pessoa: '))

a = [p1, p2, p3, p4, p5]
random.shuffle(a)

print(f'A ordem de apresentação ficou: {a}')