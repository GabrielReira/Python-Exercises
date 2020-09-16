num = int(input('Digite um número >>> '))

cont = 0
for i in range(1, num+1):
    if num % i == 0:
        cont += 1

if cont == 2:
    print('É um número primo!')
else:
    print('Não é primo.')
    print(f'Ele é divisível por {cont} números.')