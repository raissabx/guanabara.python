from datetime import date

data_atual = date.today()
ano_atual =  data_atual.year


ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano_atual - ano_nascimento

if idade < 18:
    falta = 18 - idade
    print('Você ainda não está na idade de se alistar, falta {} ano(s)'.format(falta))
    ano = ano_atual + falta
    print(f'Seu alistamento será em {ano}')

elif idade == 18:
    print('Você já pode se alistar!!')

elif idade > 18:
    passou = idade - 18
    print('Já passou {} anos do tempo de se alistar.'.format(passou))
    ano = ano_atual - passou
    print(f'Você já deveria ter se alistado há {ano} anos.')

