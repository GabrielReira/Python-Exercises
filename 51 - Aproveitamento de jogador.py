player = dict()
goals = list()

player['nome'] = input('Nome do jogador: ')
n = int(input('Quantas partidas ele jogou? '))

for i in range(1, n + 1):
    goals.append(int(input(f'Quantos gols na partida {i}? ')))
player['gols'] = goals

player['total'] = sum(player['gols'])


# Resultado para o usuário
print('-' * 30)
print(f'{player["nome"]} fez {n} partidas.')

for i, x in enumerate(player['gols']):
    print(f'> Na partida {i+1} ele marcou {x} gol(s).')
print(f'Totalizando {player["total"]} gols.')

print(f'Ele possui um aproveitamento de {player["total"] / n:.2f} gols por jogo.')