algo = input('DIGITE ALGO: ')

print('O tipo primitivo desse valor é: ', type(algo))
print('Só tem espaços? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está em maiusculas?', algo.isupper())
print('Está em minusculas?', algo.islower())
print('Está apenas com a primeira letra em maiuscula?', algo.istitle())