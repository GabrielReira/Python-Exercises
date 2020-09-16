val = int(input('Quanto de empréstimo você gostaria? R$'))
sal = int(input('Qual o seu salário mensal? '))
t   = int(input('Em quantos anos você irá pagar? '))

# O valor de cada parcela mensal não pode exceder 30% do salário.
parc = val / (t * 12)
if parc > (sal * 0.3):
    print('Empréstimo negado!')
else:
    print('Empréstimo concedido.')
    print(f'Você pagará {parc:.2f} reais por mês.')