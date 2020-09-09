# PROGRAMA QUE FAÇA A SOMA DOS DÍGITOS DE UM NÚMERO.

number = int(input('Digite um número inteiro: '))

digitsSum = 0

while number != 0:
    lastDigit = number % 10
    digitsSum += lastDigit
    numberWithoutLastDigit = number // 10
    number = numberWithoutLastDigit

    print(lastDigit, end='')
    print(f' + ' if number > 0 else ' = ', end='')

print(digitsSum)