dicionario = {
    'python': 'Uma linguagem de programação de alto nível conhecida por sua simplicidade e clareza.',
    'algoritmo': 'Um conjunto finito de etapas bem definidas para resolver um problema.',
    'inteligência artificial': 'A capacidade de um computador aprender e tomar decisões como um ser humano.',
    'criptografia': 'A técnica de proteger informações usando códigos ou cifras.'
}
solicitUsuario=input("Digite a palavra para pesquisa: ")
if solicitUsuario in dicionario:
    definição=dicionario[solicitUsuario]
    print(definição)
else:
    print("Definição nao encontrada no dicionario")