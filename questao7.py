nomes = ("feliz", "veloz", "elefante", "nariz", "raiz", "mundo", "laranja", "volante", "manga", "bengala", "limpeza")
novaTupla = tuple(x for x in nomes if len(x) > 5)
maiorQueCinco = len(novaTupla)
print(str(maiorQueCinco) + " palavras tem mais de 5 caracteres")
