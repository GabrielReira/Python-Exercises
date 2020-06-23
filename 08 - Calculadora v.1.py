# VERSÃO 1.
# PROGRAMA QUE FUNCIONE COMO UMA CALCULADORA BÁSICA.

operação = input('Digite qual operação você gostaria de realizar: \n + para adição \n - para subtração \n * para multiplicação \n / para divisão: ')
v1 = int(input('Primeiro número: '))
v2 = int(input('Segundo número: '))

if operação == '+':
    print('\nSOMA')
    print(f'{v1} + {v2} =')
    print(v1+v2)

elif operação == '-':
    print('\nSUBTRAÇÃO')
    print(f'{v1} - {v2} =')
    print(v1-v2)

elif operação == '*':
    print('\nMULTIPLICAÇÃO')
    print(f'{v1} x {v2} =')
    print(v1*v2)

elif operação == '/':
    print('\nDIVISÃO')
    print(f'{v1} ÷ {v2} =')
    print(v1/v2)

else:
    print('Você não digitou um operador válido.')
