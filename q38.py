n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro valor: {} é o maior número'.format(n1))

elif n1 < n2:
    print('O segundo valor: {} é o maior número'.format(n2))
    
else:
    print('Os dois número são iguais')