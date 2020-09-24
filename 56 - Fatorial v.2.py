# VERSÃO 2.

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


n = int(input('Digite um número: '))
print(f'{n}! = {factorial(n)}')