s = float(input('Digite o salário atual: R$'))
r = float(input('Digite a porcentagem de reajuste: '))
novo = s + s * (r / 100)

print(f'Com o reajuste de {r}%, o funcionário passa a receber R${novo:.2f}.')