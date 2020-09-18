numbers = []

n = int(input('Quantos números você deseja digitar? '))

for i in range(n):
    numbers.append(int(input(f'Digite o número da posição {i}: ')))

highest_number_pos = []
lowest_number_pos = []

for pos, number in enumerate(numbers):
    if number == max(numbers):
        highest_number_pos.append(pos)
    if number == min(numbers):
        lowest_number_pos.append(pos)


print(f'O maior número digitado foi: {max(numbers)}, na(s) posição(ões) {highest_number_pos}.')
print(f'O menor número digitado foi: {min(numbers)}, na(s) posição(ões) {lowest_number_pos}')