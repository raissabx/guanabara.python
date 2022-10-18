metros = float(input('Digite um número em metros: '))
centimetros = metros * 100
milimetros = metros * 1000

print('{} metros tem: \n {:.0f} cm \n {:.0f} mm'.format(metros, centimetros, milimetros))