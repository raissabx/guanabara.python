dias = int(input('Por quantos dias você alugou o carro: '))
km = float(input('Quantos quilômetros você rodou? '))
total = (dias * 60) + (km * 0.15)

print('O valor total é de {:.2f}'.format(total))