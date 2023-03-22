from time import sleep

n1 = int(input('* Digite o primeiro valor: '))
n2 = int(input('* Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        resultado = n1 + n2
        print(f'*** O resultado da soma é de {resultado} ***')

    elif opcao == 2:
        resultado = n1 * n2
        print(f'*** O resultado da multiplicação é de {resultado} ***')

    elif opcao == 3:
        if n1 > n2:
            print(f'*** O maior número é o {n1}! ***')
        elif n1 == n2:
            print('Os números são iguais!')
        else:
            print(f'*** O maior número é o {n2}! ***')

    elif opcao == 4:
        n1 = int(input('* Digite o primeiro valor: '))
        n2 = int(input('* Digite o segundo valor: '))

    elif opcao == 5:
        print('Finalizando...')

    else:
        print('§ Opção inválida, tente novamente! §')
    print('=-=' * 10)
sleep(2)
print('=== Fim do programa! Volte sempre! ===')
