# FAÇA UM PROGRAMA QUE AUXILIE UM JOGADOR DA MEGA-SENA A CRIAR
# PALPITES. O PROGRAMA DEVE SORTEAR UM NÚMERO X DE JOGOS, COM
# 6 NÚMEROS EM CADA JOGO.

from random import sample
from time import sleep

n = int(input('Quantos jogos você quer que eu sorteie? '))

for i in range(n):
    numbers_ms = sample(range(1, 60), 6)
    print(f'Jogo {i + 1}: {sorted(numbers_ms)}')
    sleep(1)