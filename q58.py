from random import randint

number_random = randint(0, 10)
print('IA escolheu um número entre 0 a 10!')
acertou = False
palpites = 0

while not acertou:
    chute = int(input('Tente adivinhar o número entre 0 a 10 escolhido pela IA: '))
    palpites += 1
    if chute == number_random:
        acertou = True
    else:
        if chute < number_random:
            print('Mais... Tente mais uma vez!')
        elif chute > number_random:
            print('Menos... Tente mais uma vez!')

print(f'Parabéns!!! Você é bom de chute!! Número {number_random} é o escolhido pela IA')
print(f'Você acertou em {palpites} tentativas!')
