peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
#alturaQuadrado = pow(altura, 2)
imc = peso / (altura**2)


print('Seu IMC é de {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO')

elif imc <= 25:
    print('Você está com o PESO IDEAL')

elif imc <= 30:
    print('Você está SOBREPESO')

elif imc <= 40:
    print('Você está com OBESIDADE')

elif imc > 40:
    print('Você está com OBESIDADE MÓRBIDA')


    
