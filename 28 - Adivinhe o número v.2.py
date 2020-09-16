# VERSÃO 2.

from random import randint

num = 0
pc = randint(0, 10)
tentativa = 0

print('O computador acabou de escolher um número entre 0 e 10.')

while num != pc:
    num = int(input('Tente adivinhar >>> '))
    tentativa += 1
    if num!= pc:
        print('Errou!')

if tentativa == 1:
    print('Nossa, você acertou de primeira.')
else:
    print(f'Finalmente você acertou, após {tentativa} tentativas.')