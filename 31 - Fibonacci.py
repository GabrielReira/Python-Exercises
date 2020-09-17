n = int(input('Quantos termos você deseja mostrar? >>> '))

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