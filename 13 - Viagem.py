print('As viagens possuem um valor de R$0,50 por km.')
print('Mas acima de 200km, são cobrados R$0,42 por km.')

km = int(input('Qual a quilometragem da viagem que desejas fazer? '))

if km <= 200:
    print(f'Sua viagem ficou de {km*0.5:.2f} reais.')
else:
    print(f'O valor da sua viagem é de {km*0.42:.2f} reais.')