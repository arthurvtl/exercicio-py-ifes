a = int(input('Digite quantos anos você têm: '))
m = int(input('Agora digite quantos meses você têm: '))
d = int(input('Por fim, digite quantos dias você têm: '))

ad = a*365
md = m*30

valorF = ad + md + d

print('Você está vivo há: {} dias.'.format(valorF))