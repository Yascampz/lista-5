numeros= (90,20,30,40,10,50,60,70,80)
menorNum= numeros[0]
maiorNum= numeros[0]
for x in numeros:
    if menorNum>x:
        menorNum=x
    elif maiorNum<x:
        maiorNum=x
print("menor numero é "+str(menorNum)+" e o maior numero é "+str(maiorNum))