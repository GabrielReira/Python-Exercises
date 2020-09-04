# PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALÍNDROMO,
# DESCONSIDERANDO OS ESPAÇOS.

print('='*9, 'PALÍNDROMO' ,'='*9)
frase = str(input('Digite uma frase >>> ')).strip().lower()
palavras = frase.split()
juntar = ''.join(palavras)
invert = ''
# Um for que vai rodando da última letra até a primeira
for i in range(len(juntar) - 1, -1, -1):
    invert += juntar[i]
print(f'O inverso da sua frase é {invert}.')
if juntar == invert: print('É um palíndromo!')
else: print('Não é um palíndromo...')

# OUTRA RESOLUÇÃO DO DESAFIO, SEM USO DO FOR.
frase = str(input('Digite uma frase >>> ')).strip().lower()
palavras = frase.split()
juntar = ''.join(palavras)
invert = juntar[::-1]
print(f'O inverso da sua frase é {invert}.')
if juntar == invert: print('É um palíndromo!')
else: print('Não é um palíndromo...')