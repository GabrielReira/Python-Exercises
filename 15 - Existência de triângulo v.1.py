# VERSÃO 1.
# PROGRAMA QUE PEÇA TRÊS RETAS AO USUÁRIO E DIGA SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.

print('\nDigite o valor de 3 retas para saber se elas formam um triângulo.')
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))
# Colocar numa lista ordenada crescente
lista = [v1, v2, v3]
ordem = sorted(lista)
maior, meio, menor = ordem[2], ordem[1], ordem[0]
# O maior lado deve ser menor que a soma dos outros dois
if maior < meio + menor :
    print('Pode formar um triângulo!')
else:
    print('Não pode...')