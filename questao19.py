numeros=(45,645,246,823,565,23,21,17,846,32,61,32,87,43,94)
tudoMaior=True
for x in numeros:
    if x <10:
        tudoMaior=False
if tudoMaior==True:
    print("Todos os numeros são maiores que 10")
else:
    print("Nem todos os números são maiores que 10")