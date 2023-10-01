tupla1=(1, 2, 3, 4, 5)
tupla2=(6,7,8,9,10)
tupla3=tuple(x+y for x,y in zip(tupla1,tupla2))
print(tupla3)