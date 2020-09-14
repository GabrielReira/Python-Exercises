# PROGRAMA ONDE 4 JOGADORES JOGAM UM DADO E TENHAM RESULTADOS 
# ALEATÓRIOS. OS RESULTADOS SERÃO GUARDADOS EM UM DICIONÁRIO.
# NO FINAL, COLOQUE ESSE DICIONÁRIO EM ORDEM, DO JOGADOR QUE
# TIROU O MAIOR NÚMERO NO DADO AO QUE TIROU O MENOR.

from random import randint
from time import sleep
from operator import itemgetter

games = {
    'jogador A': randint(1, 6),
    'jogador B': randint(1, 6),
    'jogador C': randint(1, 6),
    'jogador D': randint(1, 6)
}

print('VALORES SORTEADOS:')
for key, value in games.items():
    print(f'O {key} tirou {value}.')
    sleep(0.8)

ranking = sorted(games.items(), key=itemgetter(1), reverse=True)
# O ranking fica em formato de Lista.

print('RANKING:')
for i, player in enumerate(ranking):
    print(f'{i + 1}º lugar: {player[0]} com {player[1]} no dado.')
    sleep(0.5)