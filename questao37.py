filmesLancamento = {'Jurassic Park': 1993, 'Titanic': 1997, 'Avatar': 2009, 'Star Wars: Episódio IV': 1977, 'The Dark Knight': 2008}
ordem= dict(sorted(filmesLancamento.items(), key=lambda item: item[1]))
print(ordem)