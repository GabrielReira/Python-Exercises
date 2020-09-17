total = itens_caros = valor_barato = cont = 0
nome_barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))

    cont += 1
    total += preço

    if preço > 500:
        itens_caros += 1

    # O primeiro produto é cadastrado como o mais barato
    if cont == 1 or preço < valor_barato:
        valor_barato = preço
        nome_barato = produto

    c = ' '
    while c not in 'SN':
        c = str(input('Deseja cadastrar outro produto? [S/N]: ')).upper()
    if c == 'N': break

print()
print('='*10, 'PROGRAMA FINALIZADO', '='*10)
print(f'O total da compra foi: R${total:.2f}')
print(f'Temos {itens_caros} produtos custando mais de R$500.00')
print(f'O produto mais barato foi o {nome_barato}, que custa R${valor_barato:.2f}')