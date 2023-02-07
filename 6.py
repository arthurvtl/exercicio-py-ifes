import math

r = float(input('Digite o valor do raio da esfera: '))
print(' ')
print('-'*150)

v = (4/3)*math.pi*r**3

a = 4*math.pi*r**2

print(' ')
print('O valor do volume da esfera é equivalente a: {:.2f} cm³'.format(v))
print(' ')
print('O valor da área da esfera é equivalente a: {:.2f} cm²'.format(a))