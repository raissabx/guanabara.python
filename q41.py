from datetime import date

data_atual = date.today()
ano_atual =  data_atual.year

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Categoria Mirim')

elif idade <= 14:
    print('Categoria Infantil')

elif idade <= 19:
    print('Categoria Junior')

elif idade <= 20:
    print('Categoria Sênior')

else:
    print('Categoria Master')


