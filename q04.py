n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2


# :.3f é a limitação do número flutuante
print('A soma é {}, \n o produto é {} e a divisão é {:.3f}'.format(s,m,d))#, end= '') 
print('Divisão inteira {} e potência {}'.format(di, e))

