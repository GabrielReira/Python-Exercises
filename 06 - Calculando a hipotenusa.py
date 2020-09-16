import math

co = float(input('Digite o valor de um dos catetos: '))
ca = float(input('Digite o valor do outro cateto: '))

print(f'A hipotenusa mede {math.hypot(co, ca):.4f}.\n')