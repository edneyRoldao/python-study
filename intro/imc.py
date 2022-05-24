pesoInput = input('informe o peso: ')
peso = float(pesoInput)

alturaInput = input('informe a altura: ')
altura = float(alturaInput)


imc = peso / (altura ** 2)

if imc < 18:
	print('magro')
elif imc >= 18 and imc < 24:
	print('normal')
else:
	print(imc)
	print('gordo')