peso = float(input('Seu peso em kg: '))
altura = float(input('Sua altura em metros: '))
imc = peso / (altura ** 2)

print(f'Seu IMC é de {imc:.1f}.')