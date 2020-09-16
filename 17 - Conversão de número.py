num = int(input('Digite um número: '))
bas = int(input('''Escolha uma das base de conversão:
[1] para binário
[2] para octal
[3] para hexadecimal\n>>> '''))

if bas == 1:
    print(bin(num)[2:])
elif bas == 2:
    print(oct(num)[2:])
elif bas == 3:
    print(hex(num)[2:])
# O [2:] elimina os dois primeiros dígitos desnecessários.
else: 
    print('Opção inválida.')