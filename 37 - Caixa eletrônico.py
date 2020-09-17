valor = int(input('Quanto você deseja sacar? R$ '))

# Cédula inicial será a de 50.
cédula = 50
total_cédulas = 0
total_restante = valor

# Começa o programa retirando cédulas de 50.
while True:
    if total_restante >= cédula:
        total_restante -= cédula
        total_cédulas += 1
    # Quando não puder mais retirar cédulas de 50
    else:
        if total_cédulas != 0:
            print(f'{total_cédulas} cédulas de R${cédula:.2f}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total_cédulas = 0
        if total_restante == 0: break



# Outra resolução do desafio.
valor = int(input('Quanto você deseja sacar? R$ '))

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