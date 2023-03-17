numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

maior = numero1
menor = numero1

if numero2 > numero1:
    maior = numero2

if numero3 > numero1:
    maior = numero3

if numero2 < numero1:
    menor = numero2

if numero3 < numero1:
    menor = numero3

print('O número maior é o {}'.format(maior))
print('O número menor é o {}'.format(menor))