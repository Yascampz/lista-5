numeros=(1,5,45,645,2,3,5,6,246,823,565,23,21,17,846,32,61,32,87,43,94)
solicitUsuario=int(input("Digite um numero para verificarmos se esta presente na tupla:"))
presente= False
for x in numeros:
    if x == solicitUsuario:
        presente=True
if presente==True:
    print("O numero esta presente na tupla")
else:
    print("nao esta presemte na tupla")