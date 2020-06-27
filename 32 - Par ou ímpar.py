# PROGRAMA QUE FAÇA O COMPUTADOR JOGAR PAR OU ÍMPAR COM O USUÁRIO.
# O JOGO SÓ SERÁ INTERROMPIDO QUANDO O USUÁRIO PERDER, MOSTRANDO O TOTAL
# DE VITÓRIAS QUE ELE CONQUISTOU.

print('Hora de jogar par ou ímpar contra o computador.')
print('O jogo será interrompido quando você perder.')
from random import randint
from time import sleep

vitória = 0
while True:
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] >>> ')).upper()
    player = int(input('Escolha um número >>> '))
    pc = randint(0, 20)
    print('O computador escolheu... ', end='')
    sleep(1)
    print(pc)
    soma = player + pc
    print(f'A soma deu {soma}.')

    if escolha == 'P' and soma % 2 == 0:
        print('Você venceu!')
        vitória += 1
    elif escolha == 'I' and soma % 2 != 0:
        print('Você venceu!')
        vitória += 1
    else:
        sleep(1)
        print('='*8, 'GAME OVER', '='*8)
        break

sleep(1)
print(f'Total de {vitória} vitórias.')