# VERSÃO 1
# PROGRAMA QUE LEIA O PESO DE X PESSOAS E DIGA QUEM POSSUI O MAIOR E MENOR PESO.

heaviest_person = 0
lightest_person = 999

total = int(input('Qual o número de pessoas? '))

for x in range(total):
    peso = float(input(f'Peso da {x + 1}ª pessoa em kg: '))
    if peso > maior:
        maior = peso
    if peso < menor: menor = peso

print(f'A pessoa de maior peso possui {heaviest_person}kg.')
print(f'A pessoa de menor peso possui {lightest_person}kg.')