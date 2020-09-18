value = 1
all_values = []

while value != 0:
    value = int(input('Digite um valor: '))

    if value not in all_values:
        all_values.append(value)

all_values.remove(0)

print(sorted(all_values))