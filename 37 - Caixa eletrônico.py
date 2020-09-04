# PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO.
# NO INÍCIO PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR SACADO E DEPOIS O
# PROGRAMA DEVERÁ INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES.
# CONSIDERA QUE O CAIXA SÓ POSSUI CÉDULAS DE R$50, R$20, R$10 E R$1.

print('=-='*5, 'CAIXA ELETRÔNICO', '=-='*5)
valor = int(input('Quanto você deseja sacar? R$'))
# Cédula inicial será a de 50
c = 50
totalC = 0
total = valor
# Começa o programa retirando cédulas de 50
while True:
    if total >= c:
        total -= c
        totalC += 1
# Quando não puder mais retirar cédulas de 50
    else:
        if totalC != 0: print(f'{totalC} cédulas de R${c:.2f}')
        if c == 50: c = 20
        elif c == 20: c = 10
        elif c == 10: c = 1
        totalC = 0
        if total == 0: break
print('='*8, 'SAQUE FINALIZADO', '='*8)


# OUTRA RESOLUÇÃO DO DESAFIO, USANDO LÓGICA
valor = int(input('Quanto você deseja sacar? R$'))
c50 = valor // 50
valor %= 50
c20 = valor // 20
valor %= 20
c10 = valor // 10
valor %= 10
c1 = valor
if c50 != 0: print(f'{c50} cédulas de R$50.00')
if c20 != 0: print(f'{c20} cédulas de R$20.00')
if c10 != 0: print(f'{c10} cédulas de R$10.00')
if c1 != 0: print(f'{c1} cédulas de R$1.00')