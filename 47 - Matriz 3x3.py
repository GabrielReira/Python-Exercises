# PROGRAMA QUE CRIE UMA MATRIZ 3X3 E PREENCHA COM VALORES LIDOS PELO
# TECLADO. NO FINAL, MOSTRE A MATRIZ NA TELA, A SOMA DE TODOS OS VALORES
# PARES DIGITADOS, O MAIOR VALOR DA SEGUNDA LINHA E A SOMA DOS VALORES
# DA TERCEIRA COLUNA.

array = [[[],[],[]],[[],[],[]],[[],[],[]]]

sum_even = sum_third_column = 0

for i in range(3):
    for j in range(3):
        array[i][j] = int(input(f'Digite um valor para {[i]}{[j]}: '))
        
        if array[i][j] % 2 == 0:
            sum_even += array[i][j]

        if j == 2:
            sum_third_column += array[i][j]


# Exibindo a matriz criada.
print('=-='*3, 'MATRIZ 3X3', '=-='*3)
for x in range(3):
    for y in range(3):
        print(f'[{array[x][y]:^5}]', end=' ')
    print()

print(f'A soma dos valores pares é: {sum_even}')
print(f'O maior valor da segunda linha é: {max(array[1])}')
print(f'A soma dos valores da terceira coluna é: {sum_third_column}')