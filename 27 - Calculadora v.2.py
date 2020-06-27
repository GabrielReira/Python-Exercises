# VERSÃO 2.
# AGORA O PROGRAMA APRESENTA UM MENU COM A OPÇÃO PARA SABER QUAL O MAIOR NÚMERO,
# OPÇÃO PARA DIGITAR NOVOS NÚMEROS E UMA OPÇÃO PARA SAIR DO PROGRAMA.
# O PROGRAMA SÓ FINALIZARÁ QUANDO O USUÁRIO DIGITAR A OPÇÃO 7.

num1 = int(input('Digite o primeiro número >>> '))
num2 = int(input('Digite o segundo número >>> '))
menu = 0
while menu != 7:
    menu = int(input(""" O que você gostaria de fazer com esses números?
    [1] para somar
    [2] para subtrair
    [3] para multiplicar
    [4] para dividir
    [5] para saber qual o maior
    [6] para digitar novos números
    [7] para sair do programa
    """))

    if menu == 1:
        print(f'A soma desses números é igual a {num1 + num2}.')

    elif menu == 2:
        print(f'A subtração desses números é igual a {num1 - num2}.')

    elif menu == 3:
        print(f'A multiplicação desses números é igual a {num1 * num2}.')

    elif menu == 4:
        print(f'A divisão desses números é igual a {num1 / num2}.')

    elif menu == 5:
        if num1>num2: print(f'O maior número é {num1}.')
        elif num2>num1: print(f'O maior número é {num2}.')
        else: print('Por que você solicitou essa opção se eles são iguais?')

    elif menu == 6:
        num1 = int(input('Digite o primeiro número >>> '))
        num2 = int(input('Digite o segundo número >>> '))

    elif menu == 7: print(':(')

    else: print('Opção inválida.')

    print('~^~'*20)
else: print('Programa finalizado.')
