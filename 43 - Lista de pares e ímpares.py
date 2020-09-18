all_numbers = [[], []]

n = int(input('Quantos valores você gostaria de informar? '))

for i in range(1, n):
    number = int(input(f'{i}º valor: '))
    
    if number % 2 == 0:
        all_numbers[0].append(number)
    else:
        all_numbers[1].append(number)

print(f'Os valores pares são: {sorted(all_numbers[0])}')
print(f'Os valores ímpares são: {sorted(all_numbers[1])}')