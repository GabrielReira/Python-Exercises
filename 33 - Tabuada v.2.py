# VERSÃO 2.

print('O programa será encerrado caso você digite um número negativo.')

while True:
    num = int(input('Informe um número para saber sua tabuada >>> '))
    if num < 0: break

    for i in range(1, 10):
        print(f'{num} x {i} = {num*i}')