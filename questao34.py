frutasQuantidades = {'Maçã': 50,'Banana': 75,'Laranja': 60,'Morango': 40,'Pera': 55,'Uva': 70,'Abacaxi': 30,'Kiwi': 45,'Manga': 65,'Pêssego': 35}
fruta=None
maior=0
for frutas,quantidade in frutasQuantidades.items():
    if quantidade>maior:
        maior=quantidade
        fruta=frutas
print("A fruta com maior quantidade é "+ fruta)