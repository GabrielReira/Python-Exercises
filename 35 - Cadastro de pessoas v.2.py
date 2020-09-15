# VERSÃO 2.
# PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS.
# A CADA PESSOA CADASTRADA O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO
# QUER OU NÃO CONTINUAR.
# NO FINAL, MOSTRE QUANTAS PESSOAS POSSUEM MAIS DE 18 ANOS, QUANTOS HOMENS FORAM
# CADASTRADOS E QUANTAS MULHERES POSSUEM MENOS DE 21 ANOS.

c = 'S'
maior = homem = mulher = 0
while c == 'S':
    print('Cadastre uma pessoa...')

    idade = int(input('Idade: '))
    if idade >= 18: maior += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo == 'M': homem += 1
    if sexo == 'F' and idade < 21: mulher += 1

    print('-'*25)

    c = str(input('Deseja cadastrar mais alguém? [S/N]: ')).upper()

print('='*8, 'PROGRAMA FINALIZADO', '='*8)
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Homens cadastrados: {homem}')
print(f'Mulheres com menos de 21 anos: {mulher}')