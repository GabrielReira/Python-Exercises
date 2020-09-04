# PROGRAMA QUE LEIA O PESO DE 5 PESSOAS E DIGA QUEM POSSUI O MAIOR E MENOR PESO.

maior = 0
menor = 999
for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa em kg: '))
    if peso > maior: maior = peso
    if peso < menor: menor = peso
print(f'A pessoa de maior peso possui {maior} kg.')
print(f'A pessoa de menor peso possui {menor} kg.')