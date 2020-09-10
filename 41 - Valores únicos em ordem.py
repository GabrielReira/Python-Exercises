# PROGRAMA ONDE O USUÁRIO DIGITA VÁRIOS NÚMEROS E CADASTRE-OS NUMA
# LISTA. NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES ÚNICOS DIGITADOS
# E EM ORDEM CRESCENTE.
# O PROGRAMA SÓ FINALIZA SE O NÚMERO DIGITADO FOR 0.

value = 1
all_values = []

while value != 0:
    value = int(input('Digite um valor: '))
    if value not in all_values:
        all_values.append(value)

all_values.remove(0)
print(sorted(all_values))