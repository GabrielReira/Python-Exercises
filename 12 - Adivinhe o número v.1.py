# VERSÃO 1.

from random import randint

print('\nO computador escolherá um número entre 0 e 5.')
n = randint(0,5)

u = int(input('Qual número você acha que ele escolheu? '))

print('Você acertou!') if u==n else print('Você errou.')
print(f'O número que ele escolheu foi {n}.')