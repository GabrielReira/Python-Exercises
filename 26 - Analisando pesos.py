# PROGRAMA QUE LEIA O PESO DE X PESSOAS E DIGA QUEM POSSUI O MAIOR E MENOR PESO.

maior = 0
menor = 999

total = int(input('Qual o número de pessoas? '))
for x in range(total):
    peso = float(input(f'Peso da {x + 1}ª pessoa em kg: '))
    if peso > maior:
        maior = peso
    if peso < menor: menor = peso

print(f'A pessoa de maior peso possui {maior}kg.')
print(f'A pessoa de menor peso possui {menor}kg.')
