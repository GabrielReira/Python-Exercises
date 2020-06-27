# PROGRAMA QUE LEIA UM NÚMERO INTEIRO N E MOSTRE NA TELA OS N PRIMEIROS TERMOS
# DE UMA SEQUÊNCIA DE FIBONACCI.

n = int(input('Quantos termos desejas mostar? >>> '))
anterior = 0
contador = 1
# Os primeiros termos da sequência devem ser 0 e 1
t1, t2 = 0, 1
print(f'{t1} → {t2} → ', end='')
i = 0
while i < n - 2: # n - 2 pois já existem os 2 primeiros termos
    contador += anterior
    anterior = contador - anterior
    i += 1
    print(contador, end=' → ')
else: print('FIM')