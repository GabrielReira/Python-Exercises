def factorial(x):
    total = 1

    if x < 0:
        print('Erro. Fatorial negativo.')
        exit(0)
    else:
        while x > 1:
            total *= x
            x -= 1

    return total


def binomial_coefficient(n, k):
    if (n == k) or (k == 0):
        result = 1
    else:
        result = (factorial(n)) // (factorial(k) * factorial(n - k))
    
    return result



n = int(input('Valor de n: '))
k = int(input('Valor de k: '))
print(binomial_coefficient(n, k))