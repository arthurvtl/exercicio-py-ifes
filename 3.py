ap = float(input('Digite o valor da altura, em metros, da parede: '))
lp = float(input('Digite o valor da largura, em metros, da parede: '))

az = float(input('Digite o valor da altura, em metros, do azulejo: '))
lz = float(input('Digite o valor da largura, em metros, do azulejo: '))

atp = ap * lp
atz = az * lz

respf = atp // atz

print('Cabem aproximadamente {} azulejos na parede'.format(respf))