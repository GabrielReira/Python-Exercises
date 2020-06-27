# PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS E MOSTRE QUANTOS NÚMEROS FORAM
# DIGITADOS, A SOMA ENTRE ELES E SUA MÉDIA.
# O PROGRAMA SÓ DEVE FINALIZAR QUANDO O USUÁRIO DIGITAR O VALOR 999.

print('='*7, 'SOMA DE NÚMEROS', '='*7)
print('Digite vários números para saber a soma total.')
print('O programa será encerrado caso você digite 999.')

num = 0
soma = 0
quantidade = 0
while num != 999:
    soma += num
    quantidade += 1
    num = int(input())
else: print(f'Você digitou {quantidade-1} números. A soma foi {soma}.')
print(f'A média é {soma / (quantidade-1)}.')


# OUTRA RESOLUÇÃO DO DESAFIO, UTILIZANDO O COMANDO BREAK
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