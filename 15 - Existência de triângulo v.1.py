# VERSÃO 1.

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))

# Colocar numa lista ordenada crescente.
lista = [v1, v2, v3]
ordem = sorted(lista)
maior, meio, menor = ordem[2], ordem[1], ordem[0]

# O maior lado deve ser menor que a soma dos outros dois.
if maior < meio + menor :
    print('Pode formar um triângulo!')
else:
    print('Não pode...')