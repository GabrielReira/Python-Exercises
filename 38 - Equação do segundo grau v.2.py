# VERSÃO 2.
# AGORA O PROGRAMA IDENTIFICA SEPARADAMENTE A POSSIBILIDADE DO DISCRIMINANTE
# SER MENOR, MAIOR OU IGUAL A ZERO.

from math import sqrt
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

discriminant = b ** 2 - 4 * a* c

if discriminant == 0:
    root = - b / (2 * a)
    print('Delta é igual a 0. A equação possui apenas uma raiz real.')
    print(f'A raiz dessa equação é: {root}')

elif discriminant > 0:
    root1 = (- b + sqrt(discriminant)) / (2 * a)
    root2 = (- b - sqrt(discriminant)) / (2 * a)
    print('Delta é maior que 0. A equação possui duas raízes reais.')
    print(f'As raízes dessa equação são: {root1} e {root2}')

else:
    print('Delta é menor que 0.')
    print('Essa equação não possui raízes reais.')