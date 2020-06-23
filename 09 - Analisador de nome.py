# PROGRAMA QUE LEIA O NOME DA PESSOA E MOSTRE ALGUMAS INFORMAÇÕES.

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome em CAPS: {nome.upper()}')
# Quantidade de letras
print('Seu nome completo possui {} letras.' .format(len(nome) - nome.count(' ')))
# Quantidade de letras no primeiro nome
print('Seu primeiro nome possui {} letras.' .format(nome.find(' ')))
# Quantidade de letras no segundo nome
s = nome.split()
print('Seu segundo nome possui {} letras.' .format(len(s[1])))
# Silva
print('Seu nome possui Silva? {}' .format('silva' in nome.lower()))
# Primeiro e último nome
print(f'Seu primeiro nome é: {s[0]}')
print('Seu últino nome é: {}' .format(s[len(s)-1]))
