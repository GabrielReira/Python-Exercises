# VERSÃO 1.
# PROGRAMA QUE RESOLVA UMA EQUAÇÃO QUADRÁTICA.

print('EQUAÇÃO DO SEGUNDO GRAU!')
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
r1 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
r2 = (-b-(b**2-4*a*c)**(1/2))/(2*a)
print(f'As raízes desta equação são {r1} e {r2}.')