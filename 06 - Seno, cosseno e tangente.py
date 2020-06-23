# PROGRAMA QUE CALCULE O SENO, COSSENO E TANGENTE DE UM ÂNGULO DADO EM GRAUS.

import math
print('===== SEN, COS E TANG =====')
g = int(input('Digite um ângulo em graus: '))
# Precisa transformar para radianos
r = math.radians(g)
print(f'O seno de {g} é {math.sin(r):.2f}. \nO seu cosseno é {math.cos(r):.2f}. \nE sua tangente é {math.tan(r):.2f}\n')
