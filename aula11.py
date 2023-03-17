a = 2
b = 3
nome = 'Raissa'
cores = {'limpa': '\033[m', 
        'azul': '\033[34m', 
        'amarelo': '\033[33m', 
        'pretoebranco': '\033[7;30m'}

print('\033[4;30;45mOlá mundo!\033[m')
print('Os valores são \033[33m{}\033[m e \033[31m{}\033[m!!'.format(a,b))
#print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033'))
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))