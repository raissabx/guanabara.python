salario = float(input('Digite o valor do seu salário: '))

if salario > 1250.00:
    aumento = salario * 0.1
    salario_novo = aumento + salario
    print(f'Seu aumento foi de R$ {aumento:.2f} e seu novo salário é de R$ {salario_novo:.2f}')

else: 
    aumento = salario * 0.15
    salario_novo = aumento + salario
    print(f'Seu aumento foi de R$ {aumento:.2f} e seu novo salário é de R$ {salario_novo:.2f}')
