nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()

print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {}'.format(nome.find(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))