# VERSÃO 1.

number = int(input('Digite um número: '))

factorial = number
total = 1

print(f'{number}! = ', end='')

while factorial > 0:
    print(f'{factorial}', end='')
    print(' x ' if factorial > 1 else ' = ', end='')

    total *= factorial
    factorial -= 1

print(total)
