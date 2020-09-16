# VERSÃO 1.
# PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE X PESSOAS.
# NO FINAL, MOSTRE A MÉDIA DE IDADE DO GRUPO, O NOME E IDADE DO HOMEM 
# MAIS VELHO E QUANTAS MULHERES TÊM MENOS DE 20 ANOS.

totalIdade = 0.0
maisVelho = 0
nomeVelho = ''
novas = 0
nomeNova = ''

totalPessoas = int(input('Quantas pessoas você gostaria de analisar? '))

for x in range(totalPessoas):
    print(f'{x + 1}ª PESSOA')
    nome = str(input('Nome >>> '))
    idade = int(input('Idade >>> '))
    sexo = str(input('Sexo [M/F]>>> ')).lower()

    # Soma das idades.
    totalIdade += idade
    # Homem mais velho.
    if sexo == 'm' and idade > maisVelho: 
        maisVelho = idade
        nomeVelho = nome
    # Mulheres com menos de 20 anos.
    if sexo == 'f'and idade < 20: 
        novas += 1
        nomeNova = nome

# Resultado para o usuário.
print(f'\nA média de idades é {totalIdade/4:.2f}.')

print(f'O mais velho é {nomeVelho}, com {maisVelho} anos.')

if novas == 0: 
    print('Nenhuma das mulheres é menor de 20 anos.')
elif novas == 1:
    print(f'Das mulheres, apenas {nomeNova} é menor de 20 anos.')
else:
    print(f'Das mulheres, {novas} são menores de 20.')