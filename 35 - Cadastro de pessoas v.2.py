# VERSÃO 2.

maior = homem = mulher = 0
c = 'S'

while c == 'S':
    print('Cadastre uma pessoa...')

    idade = int(input('Idade: '))
    if idade >= 18: maior += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper()

    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 21:
        mulher += 1

    print('-' * 40)

    c = str(input('Deseja cadastrar mais alguém? [S/N]: ')).upper()

print()
print('='*10, 'PROGRAMA FINALIZADO', '='*10)
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Homens cadastrados: {homem}')
print(f'Mulheres com menos de 21 anos: {mulher}')