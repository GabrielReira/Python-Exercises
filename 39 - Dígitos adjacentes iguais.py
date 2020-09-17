number = int(input('Digite um número inteiro qualquer: '))

while number != 0:
    lastDigit = number % 10
    beforeLastDigit = (number % 100) // 10

    numberWithoutLastDigit = number // 10
    number = numberWithoutLastDigit

    if (lastDigit == beforeLastDigit):
        print('Esse número possui dígitos adjacentes iguais!')
        break
            
if (number == 0):
    print('Esse número não possui dígitos adjacentes iguais...')