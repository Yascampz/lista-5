contatos = {'Alice': '123-456-7890', 'Bob': '987-654-3210', 'Carol': '555-123-4567'}
nome=input("Digite o nome para removermos do dicionario: ").capitalize()
if nome in contatos:
    contatos.pop(nome)
    print(contatos)
else:
    print("Nome nao encontrado no dicionario.")