sexo = str(input('Digite seu sexo F ou M: ')).upper()[0] .strip()

while sexo not in 'FM':
    sexo = str(input('Dados inválidos. Digite seu sexo F ou M: ')).upper()[0].strip()

if sexo == 'F':
    print(f'Você é do sexo Feminino')
elif sexo == 'M':
    print(f'Você é do sexo Masculino')

