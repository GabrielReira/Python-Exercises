# PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE X PESSOAS E DIGA QUANTAS PESSOAS
# SÃO MAIORES DE IDADE, UTILIZANDO A BIBLIOTECA DE DATAS.

from datetime import date

ano = date.today().year
maior = menor = 0

total = int(input('Qual o número de pessoas? '))

for x in range(total):
    nasc = int(input(f'Em que ano a {x +1}ª pessoa nasceu? '))
    if ano - nasc < 18:
        menor += 1
    else:
        maior += 1

print(f'{maior} pessoas são maiores de idade e {menor} são menores.')