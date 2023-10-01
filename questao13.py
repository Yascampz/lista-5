numeros=(2,4,6,8,10,12,14,16,18,20)
i=0
for x in numeros:
    if x%2==0:
        i+=1
if i==len(numeros):
    print ("Todos os numeros são pares")