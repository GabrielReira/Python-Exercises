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
        print('GAME OVER.')
        break

sleep(1)
print(f'Total de {vitória} vitória(s).')