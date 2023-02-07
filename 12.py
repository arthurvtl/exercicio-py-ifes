vc = float(input('Digite quantos carros você vendeu: '))
vv = float(input('Digite o valor total de suas vendas: '))
s = float(input('Digite o valor do seu sálario fixo: '))
c = 0.005 * vv

valF = s + c * vc + ((5*vv)/100)

print('O valor final do seu sálario é de: R${}'.format(valF))