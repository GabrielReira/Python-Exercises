soma = 0
cont = 0

for n in range(0, 500, 3):
    if n % 2 != 0:
        soma += n
        cont += 1

print(f'O total de número contados foi {cont} e seu somatório deu {soma}.')