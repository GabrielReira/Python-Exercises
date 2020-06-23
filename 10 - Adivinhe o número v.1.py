# VERSÃO 1.
# PROGRAMA QUE FAÇA O USUÁRIO TENTAR ADIVINHAR O NÚMERO QUE O 
# COMPUTADOR ESCOLHEU ENTRE 0 E 5.

from random import randint
print('\nO computador escolherá um número entre 0 e 5.')
u = int(input('Qual número você acha que ele escolheu? '))
n = randint(0,5)
print('Você acertou!') if u==n else print('Você errou.')
print(f'O número que ele escolheu foi {n}.')