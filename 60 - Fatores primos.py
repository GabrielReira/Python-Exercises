número = 0
while número <= 0:
    número = int(input('Número inteiro maior que 0: '))

fator = 2

print(f'{número} = ', end='')

while número > 1:
    multiplicidade = 0

    while número % fator == 0:
        número = número / fator
        multiplicidade += 1

    if multiplicidade > 0:
        print(f'{fator}^{multiplicidade}', end=' * ')

    fator += 1

print(1)