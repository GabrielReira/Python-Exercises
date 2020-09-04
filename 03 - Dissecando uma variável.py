# PROGRAMA QUE LEIA O QUE O USUÁRIO DIGITOU E DIGA TODAS AS INFORMAÇÕES
# POSSÍVEIS SOBRE.

print('====== O QUE VOCÊ DIGITOU É... ======')
p = input('Digite algo: ')
print('Tipo primitivo desse valor:', type(p))
print('É um número?', p.isnumeric())
print('Possui apenas espaços?', p.isspace())
print('É formado por apenas letras?', p.isalpha())
print('Caso seja apenas letras:')
print('Estão todas as letras em minúsuclo?', p.islower())
print('Estão todas as letras em maiúsculo?', p.isupper())
print('Está capitalizada?', p.istitle())

# OUTRA RESOLUÇÃO DO DESAFIO.
q = input('Digite algo: ')
print(f'Tipo primitivo desse valor: {type(q)}')
print(f'É um número? {q.isnumeric()}')
print(f'É formado apenas por letras? {q.isalpha()}')
print(f'Possui apenas espaços? {q.isspace()}')
