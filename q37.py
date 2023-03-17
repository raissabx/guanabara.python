numero = int(input('Digite um número inteiro: '))

conversao = int(input('Digite qual a convesão que deseja: 1- BINÁRIO, 2- OCTAL, 3- HEXADECIMAL: '))

if conversao == 1:
    binario = format(numero, 'b')
    print('O número {} em Binário é {}'.format(numero, binario))

elif conversao == 2:
    octal = format(numero, 'o')
    print('O número {} em Octal é {}'.format(numero, octal))

elif conversao == 3:
    hexa = format(numero, 'x')
    print('O número {} em Hexadecimal é {}'.format(numero, hexa))


