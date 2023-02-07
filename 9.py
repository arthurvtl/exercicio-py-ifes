m = float(input('Digite quantas maçãs você comprou: '))
print(' ')
b = float(input('Digite quantos kg de banana você comprou: '))

valorM = m*1.30
valorB = b*5
valorF = valorM + valorB

print('O valor final da sua compra foi de: R${}'.format(valorF))