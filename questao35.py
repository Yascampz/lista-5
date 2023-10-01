alimentosCalorias = {'Maçã': 52, 'Banana': 89, 'Laranja': 43, 'Morango': 32, 'Pera': 57, 'Uva': 69, 'Abacaxi': 50, 'Kiwi': 61, 'Manga': 60, 'Pêssego': 39, 'Cenoura': 41, 'Brócolis': 34, 'Espinafre': 23, 'Batata': 77, 'Arroz': 130, 'Frango': 165, 'Peixe': 105, 'Ovo': 147, 'Iogurte': 61, 'Leite': 42}
somaCalorias=0
for x in alimentosCalorias.values():
    somaCalorias+=x
print("a soma dos valores é "+str(somaCalorias))