# PROGRAMA QUE CALCULE A HIPOTENUSA A PARTIR DOS VALORES DOS CATETOS,
# UTILIZANDO A BIBLIOTECA DE MATEMÁTICA.

import math
print('===== CALCULANDO A HIPOTENUSA =====')
co = float(input('Digite o valor de um dos catetos: '))
ca = float(input('Digite o valor do outro cateto: '))
print(f'A hipotenusa mede {math.hypot(co, ca):.4f}.\n')