# PROGRAMA QUE LEIA O NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE TUDO EM 
# UMA ÚNICA LISTA FORMADA COM TRÊS NÍVEIS. 
# AO FINAL, EXIBA O BOLETIM COM A MÉDIA DE CADA ALUNO.

# LISTA COM TRÊS DIMENSÕES.
# Exemplo de como a lista de estudantes deve ficar:
# estudantes = [['Maria', [10.0, 8.0], 9.0], ['João', [4.5, 9.5], 7.0]]
# print(estudantes[1][1][1]) # Imprime a segunda nota de João (9.5)


studants = list()

while True:
    name = str(input('Nome: '))

    score1 = float(input('Nota 1: '))
    score2 = float(input('Nota 2: '))

    average_score = (score1 + score2) / 2
    studants.append([name, [score1, score2], average_score])

    answer = ' '
    while answer not in 'SN':
        answer = input('Quer continuar? [S/N] ').upper()
    if answer == 'N':
        break

# Resultado para o usuário com o boletim formatado.
print('\n', '=-='*4, 'BOLETIM', '=-='*4, '\n')
print(f'{"ÍNDICE":<8}{"NOME":<15}{"MÉDIA":>10}')
print('-' * 35)

# Exibir na tela o índice do aluno, seu nome e sua média.
for i in range(len(studants)):
    print(f'{i:<8}{studants[i][0]:<15}{studants[i][2]:>9}')

# Perguntar ao usuário se ele gostaria de ver quais foram as notas de algum aluno.
while True:
    print('-' * 35)

    index = int(input(f'''Gostaria de ver as notas 1 e 2 de alguém? (999 para interromper)
Digite o índice do respectivo aluno, de 0 à {len(studants) - 1}: '''))

    if index == 999:
        break

    if index <= (len(studants) - 1):
        print(f'Notas de {studants[index][0]}: {studants[index][1]}')