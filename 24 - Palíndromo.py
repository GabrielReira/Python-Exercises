frase = str(input('Digite uma frase (sem acentos) >>> ')).strip().lower()

palavras = frase.split()
juntar = ''.join(palavras)
invert = ''

# Um for que vai rodando da última letra até a primeira.
for i in range(len(juntar) - 1, -1, -1):
    invert += juntar[i]

print(f'O inverso da sua frase é {invert}.')

if juntar == invert: 
    print('É um palíndromo!')
else: 
    print('Não é um palíndromo...')


# Outra resolução do desafio, sem uso do for.
frase = str(input('Digite uma frase (sem acentos) >>> ')).strip().lower()

palavras = frase.split()
juntar = ''.join(palavras)
invert = juntar[::-1]

print(f'O inverso da sua frase é {invert}.')

if juntar == invert: 
    print('É um palíndromo!')
else: 
    print('Não é um palíndromo...')