# PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCÁ-LOS EM DUAS LISTAS
# DISTINTA DE PARES E ÍMPARES.
# O PROGRAMA DEVE FINALIZAR SE O USUÁRIO DIGITAR 0.

number = 1
all_numbers = []
even_numbers = []
odd_numbers = []

while number != 0:
    number = int(input('Digite um valor: '))
    all_numbers.append(number)
all_numbers.remove(0)

for number in all_numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(f'Os números digitados foram: {all_numbers}')
print(f'Os números pares são: {even_numbers}')
print(f'Os números ímpares são: {odd_numbers}')