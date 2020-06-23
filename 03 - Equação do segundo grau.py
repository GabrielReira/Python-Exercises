# PROGRAMA QUE RESOLVA UMA EQUAÇÃO QUADRÁTICA.

print('EQUAÇÃO DO SEGUNDO GRAU!')
a = int(input('Digite o número que vem acompanhado por x ao quadrado: '))
b = int(input('Agora o que vem acompanhado somente por x: '))
c = int(input('Agora o termo independente: '))
r1 = int((-b+(b**2-4*a*c)**(1/2))/(2*a))
r2 = int((-b-(b**2-4*a*c)**(1/2))/(2*a))
print(f'As raízes desta equação são {r1} e {r2}.')
