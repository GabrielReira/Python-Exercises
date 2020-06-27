# PROGRAMA QUE LEIA DOIS NÚMEROS E MOSTRE UM MENU COM ALGUMAS OPÇÕES DE OPERAÇÕES
# ENTRE ELES.
# O PROGRAMA SÓ FINALIZARÁ QUANDO O USUÁRIO DIGITAR A OPÇÃO 5.

num1 = int(input('Digite o primeiro número >>> '))
num2 = int(input('Digite o segundo número >>> '))
menu = 0
while menu != 5:
    menu = int(input(""" O que você gostaria de fazer com esses números?
    [1] para somar
    [2] para multiplicar
    [3] para saber qual o maior
    [4] para digitar novos números
    [5] para sair do programa
     """))
    if menu == 1:
        print(f'A soma desses números é igual a {num1+num2}.')

    elif menu == 2:
        print(f'A multiplicação desses números é igual a {num1*num2}.')

    elif menu == 3:
        if num1>num2: print(f'O maior número é {num1}.')
        elif num2>num1: print(f'O maior número é {num2}.')
        else: print('Por que você solicitou essa opção se eles são iguais?')

    elif menu == 4:
        num1 = int(input('Digite o primeiro número >>> '))
        num2 = int(input('Digite o segundo número >>> '))

    elif menu == 5: print(':(')

    else: print('Opção inválida.')
    print('~^~'*20)
else: print('Programa finalizado.')