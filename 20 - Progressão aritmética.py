# PROGRAMA QUE PEÇA AO USUÁRIO O PRIMEIRO TERMO DE UMA PROGRESSÃO
# ARITMÉTICA E SUA RAZÃO, DEPOIS CALCULE SEUS 10 PRIMEIROS TERMOS.

a = int(input('Digite o primeiro termo da PA >>> '))
r = int(input('Digite a razão da PA >>> '))
for i in range(10):
    print(a)
    a += r
else: print('Esses foram os 10 primeiros termos da PA.')

# OUTRA RESOLUÇÃO DO DESAFIO, UTILIZANDO O WHILE.
a = int(input('Digite o primeiro termo da PA >>> '))
r = int(input('Digite a razão da PA >>> '))
i = 0
while i<10:
    print(a)
    a += r
    i += 1
else: print('Esses foram os 10 primeiros termos da PA.')