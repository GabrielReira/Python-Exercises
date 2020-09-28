def is_prime(number):
    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False


def prime_counter(x):
    total = 0

    for i in range(1, x + 1):
        if is_prime(i):
            total += 1

    return total


x = int(input('Digite um valor: '))
print(prime_counter(x))