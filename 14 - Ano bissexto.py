ano = int(input('Digite um ano para saber se ele é bissexto: '))

# Não é bissexto anos múltiplos de 100 que não são múltiplos de 400.
# Por exemplo: 1700, 1800, 1900 não são anos bissextos.

if ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0):
    print('Sim.')
else:
    print('Não.')