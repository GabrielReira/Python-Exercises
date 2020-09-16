import math

g = int(input('Digite um ângulo em graus: '))
# Precisa transformar o ângulo para radianos.
r = math.radians(g)

print(f'''O seno de {g} é {math.sin(r):.2f}.
O seu cosseno é {math.cos(r):.2f}.
E sua tangente é {math.tan(r):.2f}.''')