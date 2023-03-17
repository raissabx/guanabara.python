velocidade_media = float(input('Digite a velocidade média do seu carro: '))

if velocidade_media > 80:
    print('Você ultrapassou a velocidade permitida de 80km/h.')
    multa = (velocidade_media - 80) * 7
    print('Você será multado no valor de R$ {:.2f}'.format(multa))

else: 
    print('Parabéns! Você está respeitando as leis de transito!')