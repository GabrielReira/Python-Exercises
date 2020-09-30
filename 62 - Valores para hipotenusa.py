def é_hipotenusa(a, b ,c):
    if (c**2 == a**2 + b**2):
        return True
    else:
        return False


def hipotenusas(n):
    valores = list()

    a, b, c = 1, 1, 1

    while a < n:
        while b < n:
            while c <= n:
                if é_hipotenusa(a, b, c) and (c not in valores):
                    valores.append(c)
                c += 1
            b += 1
            c = 1
        a += 1
        b = 1
    
    return sorted(valores)


n = int(input('Valor: '))
print(f'De 1 a {n} existem as hipotenusas: {hipotenusas(n)}')