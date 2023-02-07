n1 = float(input('Digite o valor da sua nota do primeiro trimestre: '))
print(' ')
n2 = float(input('Digite o valor da sua nota do segundo trimestre: '))
print(' ')
ativ = float(input('Digite o valor atríbuido a suas atividades: '))

m = (4*n1+3*n2+2*ativ) / 9

print('-'*150)
print(' ')
print('O valor da sua média foi de: {:.2f}'.format(m))

