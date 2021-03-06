# VERSÃO 3.

person = dict()
people = list()

while True:
    person['nome'] = input('Nome: ').capitalize()

    person['idade'] = int(input('Idade: '))

    sex = ' '
    while sex not in 'MF':
        sex = input('Sexo [M/F]: ').upper()
        person['sexo'] = sex

    # Adicionar a pessoa a lista de pessoas.
    people.append(person.copy())

    answer = ' '
    while answer not in 'SN':
        answer = input('Quer continuar? [S/N]: ').upper()
    if answer == 'N':
        break


# Total de pessoas
print(f'1) O grupo possui {len(people)} pessoas.')

# Média de idade
age_sum = 0
for each in people:
    age_sum += each['idade']
print(f'2) A média de idade do grupo é {age_sum / len(people):.1f} anos.')

# Mulheres cadastradas
print('3) As mulheres cadastradas foram: ', end='')
for each in people:
    if each['sexo'] == 'F':
        print(f'[{each["nome"]}]', end=' ')

# Pessoas maiores de idade
print('\n4) As pessoas maiores de idade são: ')
for each in people:
    if each['idade'] >= 18:
        print(f'- {each["nome"]} com {each["idade"]} anos de idade')