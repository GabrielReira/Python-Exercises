# PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE 7 PESSOAS E QUANTAS PESSOAS SÃO
# MAIORES DE IDADE, UTILIZANDO A BIBLIOTECA DE DATAS.

from datetime import date
ano = date.today().year
maior = 0
menor = 0
for x in range(1, 8):
    nasc = int(input(f'Em que ano a {x}ª pessoa nasceu? >>> '))
    if ano - nasc < 18 : menor += 1
    else: maior += 1
print(f'{maior} pessoas são maiores de idade e {menor} são menores.')