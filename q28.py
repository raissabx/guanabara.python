from random import randint
from time import sleep


number_random = randint(0, 10)
chute = int(input('Tente adivinhar o número entre 0 a 10 escolhido pela IA: '))
print('Processando...')
sleep(3)
if chute == number_random:
    print('Parabéns!!! Você é bom de chute!! O número é o {}'.format(chute))

elif chute < number_random:
    print('Eita! Acho q você chutou um número muito abaixo! O número escolhido é o {}'.format(number_random))

else:
    print('Uiii!! Você chutou longe hein! O número escolhido é o {}'.format(number_random))