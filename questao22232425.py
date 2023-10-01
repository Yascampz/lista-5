nomeIdade={"Yasmin":17,"João":8,"Camilla":34,"Leonardo":31,"Gesilene":55,"Jonas":54}
print(nomeIdade)
print(nomeIdade.keys())
print(nomeIdade.values())
solicitUsuario= input("Digite o nome da pessoa que deseja encontrar a idade: ").capitalize()
if solicitUsuario in nomeIdade:
    idade=nomeIdade[solicitUsuario]
    print("A idade de "+ solicitUsuario +" é "+str(idade))
else:
    print("O nome digitado nao foi encontrado")
