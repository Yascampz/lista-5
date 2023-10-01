produtosEstoque = {'Camiseta': 100,'Calça Jeans': 50,'Tênis': 75,'Mochila': 30,'Boné': 60, 'Óculos de Sol': 40,'Relógio': 20,'Celular': 90,'Tablet': 15,'Fones de Ouvido': 70}
valorEspecífico=50
estoqueAbaixo={}
for produto, estoque in produtosEstoque.items():
    if estoque < valorEspecífico:
        estoqueAbaixo[produto] = estoque
print(estoqueAbaixo)