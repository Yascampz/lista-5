produtosValores={'Maçã': 2.50,'Banana': 1.20,'Laranja': 3.00,'Morango': 4.50,'Pera': 2.80}
somaValores=0
for x in produtosValores.values():
    somaValores+=x
print("a soma dos valores é "+str(somaValores))