nome = str(input('Digite seu nome completo: ')).strip()

# Quantidade de letras.
print('Seu nome completo possui {} letras.' .format(len(nome) - nome.count(' ')))

# Primeiro nome e quantidade de letras.
s = nome.split()
print(f'Seu primeiro nome é: {s[0]}')
print('Seu primeiro nome possui {} letras.' .format(nome.find(' ')))

# Quantidade de letras no último nome.
print('Seu último nome é: {}' .format(s[len(s) - 1]))
print('Seu último nome possui {} letras.' .format(len(s[-1])))

# Se o nome possui Silva.
print('Seu nome possui Silva? {}' .format('silva' in nome.lower()))