paisesCapitais = {'Brasil': 'Brasília','Estados Unidos': 'Washington, D.C.','França': 'Paris','Japão': 'Tóquio','Austrália': 'Camberra','Índia': 'Nova Deli','Itália': 'Roma','Alemanha': 'Berlim','Reino Unido': 'Londres','Canadá': 'Ottawa'}
solicitUsuario=input("Digite o País para pesquisa: ").capitalize()
if solicitUsuario in paisesCapitais:
    capital=paisesCapitais[solicitUsuario]
    print(capital)
else:
    print("capital nao encontrada no dicionario")