# PROGRAMA QUE MOSTRE QUANTOS NÚMEROS ÍMPARES E MÚLTIPLOS DE 3 EXISTEM NO INTERVALO
# DE 1 ATÉ 500, E QUAL A SOMA ENTRE ELES.

s = 0
cont = 0
for n in range(0, 500, 3):
    if n%2 != 0:
        s += n
        cont += 1
else: print(f'O total de número contados foi {cont} e seu somatório deu {s}.')