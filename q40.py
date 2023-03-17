n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/2

if media < 5.0:
    print('Sua média foi de {}. Você está REPROVADO!'.format(media))

elif 7 > media >= 5:
    print('Sua média foi de {}. Você está RECUPERAÇÃO!'.format(media))

elif media >= 7.0:
    print('Sua média foi de {}. Você está APROVADO!'.format(media))

