valor_produto = float(input('Digite o valor do produto: '))

pagamento = int(input('''Forma de pagamento -> 
A vista dinheiro/cheque - 1 | 
A vista cartão - 2 | 
Dividir em até 2x - 3 | 
Dividir em 3x ou mais - 4: '''))

if pagamento == 1:
    desconto = valor_produto * 0.1
    valor_final = valor_produto - desconto
    print('O valor com desconto é de R$ {}'.format(valor_final))

elif pagamento == 2:
    desconto = valor_produto * 0.05
    valor_final = valor_produto - desconto
    print('O valor com desconto é de R$ {}'.format(valor_final))

elif pagamento == 3:
    print('Não há descontos. Valor a pagar {}'.format(valor_produto))

elif pagamento == 4:
    juros = valor_produto * 0.2
    valor_final = valor_produto + juros
    print('O valor com juros é de R$ {}'.format(valor_final))

else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE')