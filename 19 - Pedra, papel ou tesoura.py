from random import randint
from time import sleep

print('='*5, 'JO KEN PÔ', '='*5)
player = int(input('''Escolha sabiamente
1 para PEDRA
2 para PAPEL
3 para TESOURA
>>> '''))

itensPC = ('pedra', 'papel', 'tesoura')
pc = randint(1, 3)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print(f'O computador escolheu {itensPC[pc-1]}.')

if pc == player: print('Deu empate.')
elif pc == 1:
    if player == 2: print('Você ganhou...')
    elif player == 3: print('Haha. Loser!')
    else: print ('Sua jogada foi inválida.')
elif pc == 2:
    if player == 1: print('Haha. Loser!')
    elif player == 3: print('Você ganhou...')
    else: print ('Sua jogada foi inválida.')
elif pc == 3:
    if player == 1: print('Você ganhou...')
    elif player == 2: print('Haha. Loser!')
    else: print ('Sua jogada foi inválida.')