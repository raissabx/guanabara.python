from datetime import date

atual = date.today().year
tot_maior = 0
tot_menor = 0

for pessoas in range(1, 8):
    nasc = int(input(f'Em que ano a pessoa {pessoas}ª nasceu: '))
    idade = atual - nasc
    
    if idade >= 18:
        tot_maior += 1
    else:
        tot_menor += 1


print(f'Ao todo tivemos {tot_maior} pessoas maiores de idade')
print(f'Ao todo tivemos {tot_menor} pessoas menores de idade')
