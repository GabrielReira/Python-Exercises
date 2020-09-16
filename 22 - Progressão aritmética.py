# VERSÃO 1.

a = int(input('Digite o primeiro termo da PA >>> '))
r = int(input('Digite a razão da PA >>> '))

for i in range(10):
    print(a)
    a += r
else: print('Esses foram os 10 primeiros termos da PA.')


# Outra resolução do desafio, utilizando o while.
a = int(input('Digite o primeiro termo da PA >>> '))
r = int(input('Digite a razão da PA >>> '))

i = 0
while i < 10:
    print(a)
    a += r
    i += 1
else: print('Esses foram os 10 primeiros termos da PA.')