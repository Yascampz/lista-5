tupla=("Maçã", "Banana", "Laranja","Pêra", "Uva", "Morango", "Abacaxi", "Melancia", "Manga", "Kiwi")
solicitUsuario=input("Digite o nome de uma fruta para verificarmos a posição na tupla: ").capitalize()
if solicitUsuario in tupla:
        posição= tupla.index(solicitUsuario) + 1       
        print("A fruta está na " + str(posição) + "º posição da tupla")
else:
        print("A fruta não esta na tupla")