# VERSÃO 2.

def arithmetic_prog(first_term, last_term, common_diff):
    # Evitar que o programa entre em loop.
    if common_diff == 0:
        print('Razão inválida.')
        exit(0)

    # Razão positiva.
    if first_term <= last_term:
        # Evitar que o programa entre em loop.
        if common_diff < 0:
            print('Razão inválida.')
            exit(0)

        while first_term <= last_term:
            print(first_term, end=' → ')
            first_term += common_diff
        print('FIM!')

    # Razão negativa.
    else:
        # Evitar que o programa entre em loop.
        if common_diff > 0:
            print('Razão inválida.')
            exit(0)

        while first_term >= last_term:
            print(first_term, end=' → ')
            first_term += common_diff
        print('FIM!')

ft = int(input('Primeiro termo: '))
lt = int(input('Último termo: '))
cd = int(input('Razão: '))
arithmetic_prog(ft, lt, cd)


# Utilizando o range().
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Razão: '))
for x in range(a, b, c):
    print(x, end=' → ')
print('FIM!')