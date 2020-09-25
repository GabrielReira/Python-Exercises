def row(msg):
    len_row = len(msg) + 6

    print('~' * len_row)
    print(f'{msg:^{len_row}}') # Centralizar o texto entre as linhas
    print('~' * len_row)


def print_help(x):
    print('\033[7;40m', end='') # Adicionar fundo branco ao manual
    help(x)
    print('\033[m') # Retirar estilização



while True:
    search = input('Pesquise por uma Função ou Biblioteca: ').lower()

    if search != 'fim':
        row(f"Manual do comando '{search}'")
        print_help(search)
    else:
        break