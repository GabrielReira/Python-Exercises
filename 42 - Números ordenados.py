# PROGRAMA ONDE O USUÁRIO DIGITA VÁRIOS NÚMEROS E CADASTRE-OS EM UMA
# LISTA JÁ NA POSIÇÃO CORRETA DE ORDEM CRESCENTE DE VALORES.
# NÃO PODE USAR O MÉTODO SORT().

all_values = []

n = int(input('Quantos valores você deseja digitar? '))

for i in range(n):
    value = int(input('Digite um valor: '))
    
    # Se for o primeiro item ou se for maior que o último valor
    if (i == 0) or (value > all_values[-1]):
        all_values.append(value)
    # Se estiver entre os itens do meio
    else:
        list_index = 0
        while list_index < len(all_values):
            if value <= all_values[list_index]:
                all_values.insert(list_index, value)
                break
            list_index += 1

print(all_values)