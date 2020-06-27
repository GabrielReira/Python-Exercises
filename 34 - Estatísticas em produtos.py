# PROGRAMA QUE LEIA O NOME E O PREÇO EM VÁRIOS PRODUTOS.
# O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CADASTRAR OU NÃO MAIS PRODUTOS.
# NO FINAL, MOSTRE QUAL FOI O TOTAL GASTO, QUANTOS PRODUTOS CUSTAM MAIS DE R$500,
# E QUAL FOI O PRODUTO MAIS BARATO.

print('=-='*5, 'COMPRAS', '=-='*5)
total = caro = barato = cont = 0
nomeB = ''
while True:
    produto = str(input('Nome do produto: '))

    preço = int(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 500: caro += 1
    # O primeiro produto é cadastrado como o mais barato
    if cont == 1 or preço < barato:
        barato = preço
        nomeB = produto

    c = ' '
    while c not in 'SN':
        c = str(input('Deseja cadastrar outro produto? [S/N]: ')).upper()
    if c == 'N': break

print('='*10, 'PROGRAMA FINALIZADO', '='*10)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$500.00')
print(f'O produto mais barato foi o {nomeB}, que custa {barato:.2f}')