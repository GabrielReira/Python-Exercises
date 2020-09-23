def highest_prime(number):
    # O loop para verificar o maior primo começa no próprio número
    # e vai decrescendo.
    for i in range(number, 1, -1):
        # O contador indica o número de múltiplos que o número possui.
        count = 0

        # Esse número será dividido por todos os números até
        # chegar nele próprio.
        for j in range(1, i + 1):
            if (i % j == 0):
                count += 1
                # Se possuir mais que dois divisores já sabemos que
                # o número não é primo.
                if count > 2:
                    break
        # Se possuir apenas dois divisores ele é primo.
        if count == 2:
            return i


n = int(input('Digite um valor: '))
print(highest_prime(n))