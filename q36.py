valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite em quantos anos vc irá pagar: '))

meses = anos * 12
prestacao = valor_casa / meses
porcentagem = salario * 0.3

if prestacao > porcentagem:
    print('EMPRESTIMO NEGADO!')
    
else:
    print('EMPRESTIMO APROVADO!')
    print('Suas prestações mensais será de R$ {:.2f}'.format(prestacao))
