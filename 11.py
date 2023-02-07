cf = float(input('Digite o custo de fábrica deste carro: '))

pdd = (cf * 0.28) + cf
imp = (cf * 0.45) + cf

valorF = pdd + imp + cf

print('O  valor final de compra deste carro aplicado os impostos é de: R${}'.format(valorF))
