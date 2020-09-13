# VERSÃO 2.
# AGORA O PROGRAMA DEVE ARMAZENAR O NOME E PESO DE TODAS AS 
# PESSOAS EM UMA LISTA E EXIBIR AO FINAL O TOTAL DE PESSOAS,
# AQUELAS COM MAIS DE 90KG E AS COM MENOS DE 60KG.

people = list()
people_data = list()

while True:
    name = str(input('Nome: '))
    people_data.append(name)
    weight = float(input('Peso: '))
    people_data.append(weight)

    # Inserir o nome e idade da pessoa na lista 'people' e 
    # depois zerar a lista 'people_data' para cadastra outra pessoa.
    people.append(people_data[:])
    people_data.clear()

    answer = ' '
    while answer not in 'SN':
        answer = input('Deseja cadastrar mais alguém? [S/N] ').upper()
    if answer == 'N': break


# Fazer um loop em todas as pessoas comparando apenas seus pesos.
# Armazenar o menor e o maior peso em variáveis.
greater_weight = lower_weight = 0

for p in people:
    # A primeira pessoa é quem possui o maior e menor peso, já que só tem ela.
    if p[1] in people[0]: # Primeiro loop.
        greater_weight = lower_weight = p[1]
    elif p[1] > greater_weight:
        greater_weight = p[1]
    elif p[1] < lower_weight:
        lower_weight = p[1]


# Resultado para o usuário
print('\n','=-='*8, 'RESULTADO', '=-='*8, '\n')
print(f'Total de {len(people)} pessoas.')
print(f'O menor peso registrado foi {lower_weight}kg e o maior {greater_weight}kg.')
print(f'As pessoas com mais de 90kg são: ', end='')
for p in people:
    if p[1] > 90:
        print(f'[{p[0]}]', end='')
print(f'\nAs pessoas com menos de 60kg são: ', end='')
for p in people:
    if p[1] < 60:
        print(f'[{p[0]}]', end='')