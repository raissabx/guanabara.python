from random import randint

pc = randint(0, 2)
jogador = int(input('''Escolha -> 
0 - Pedra, 1 - Papel, 2 - Tesoura: '''))

if pc == 0:
    if jogador == 0:
        print('Sua escolha: Pedra')
        print('Escolha da IA: Pedra')
        print('*EMPATE* -> Pedra com Pedra')

    elif jogador == 1:
        print('Sua escolha: Papel')
        print('Escolha da IA: Pedra')
        print('*VOCÊ VENCEU* -> Papel embrulha Pedra')

    elif jogador == 2:
        print('Sua escolha: Tesoura')
        print('Escolha da IA: Pedra')
        print('*IA VENCEU* -> Pedra quebra Tesoura')

if pc == 1:
    if jogador == 0:
        print('Sua escolha: Pedra')
        print('Escolha da IA: Papel')
        print('*IA VENCEU* -> Papel embrulha Pedra')

    elif jogador == 1:
        print('Sua escolha: Papel')
        print('Escolha da IA: Papel')
        print('*EMPATE* -> Papel com Papel')

    elif jogador == 2:
        print('Sua escolha: Tesoura')
        print('Escolha da IA: Papel')
        print('*VOCÊ VENCEU* -> Tesoura corta Papel')

if pc == 2:
    if jogador == 0:
        print('Sua escolha: Pedra')
        print('Escolha da IA: Tesoura')
        print('*VOCÊ VENCEU* -> Pedra quebra Tesoura')

    elif jogador == 1:
        print('Sua escolha: Papel')
        print('Escolha da IA: Tesoura')
        print('*IA VENCEU* -> Tesoura corta Papel')

    elif jogador == 2:
        print('Sua escolha: Tesoura')
        print('Escolha da IA: Tesoura')
        print('*EMPATE* -> Tesoura com Tesoura')


