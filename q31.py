viagem = float(input('Qual é a distância da sua viagem em Km: '))

if viagem <= 200:
    passagem = viagem * 0.50
    print('O valor da sua passagem é de R$ {:.2f}'.format(passagem))

else:
    passagem = viagem * 0.45
    print('O valor da sua passagem é de R$ {:.2f}'.format(passagem))
