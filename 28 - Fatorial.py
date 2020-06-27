# PROGRAMA QUE LEIA UM NÚMERO E MOSTRE O SEU CÁLCULO FATORIAL.

num = int(input('Digite um número >>> '))
fatorial = num
total = 1
print(f'{num}! = ', end='')
while fatorial > 0:
    print(f'{fatorial}', end='')
    print(' x ' if fatorial > 1 else ' = ', end='')
    total *= fatorial
    fatorial -= 1
else: print(total)