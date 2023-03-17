soma = 0
count = 0

for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        count += 1
print(f'Você digitou {count} números e a soma deles é de {soma}!')
