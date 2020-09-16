heaviest_person = 0
lightest_person = 999

total = int(input('Qual o número de pessoas? '))

for x in range(total):
    weight = float(input(f'Peso da {x + 1}ª pessoa em kg: '))
    if weight > heaviest_person:
        heaviest_person = weight
    if weight < lightest_person: 
        lightest_person = weight

print(f'A pessoa de maior peso possui {heaviest_person}kg.')
print(f'A pessoa de menor peso possui {lightest_person}kg.')