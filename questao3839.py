jogadoresGols = {'Neymar': 25, 'Messi': 30, 'Ronaldo': 20, 'Mbappé': 18, 'Salah': 22}
jogador=None
maior=0
for jogadores,gols in jogadoresGols.items():
    if gols>maior:
        maior=gols
        jogador=jogadores
print("O jogador com mais gols é "+ jogador)