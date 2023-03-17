soma_idade = 0
media_idade = 0
maior_idadeH = 0
nome_velho = ''
tot_mulher20 = 0

for p in range(1, 5):
    print(f'--------{p}ª PESSOA--------')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    soma_idade += idade

    if p == 1 and sexo in 'Mm':
        maior_idadeH = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idadeH:
        maior_idadeH = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        tot_mulher20 += 1


media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade} anos')
print(f'O homem mais velho tem {maior_idadeH} anos e se chama {nome_velho}')
print(f'Ao todo são {tot_mulher20} mulheres com menos de 20 anos.')


