print('Digite vários números para saber a soma total.')
print('O programa será encerrado caso você digite 999.')

soma = quantidade = 0

while True:
    num = int(input())
    if num == 999: break

    soma += num
    quantidade += 1

print(f'A soma dos {quantidade} valores é {soma}.')
print(f'A média é {soma / quantidade}.')