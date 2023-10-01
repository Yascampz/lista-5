paisesPop = (
    ("China", 1444216), ("Índia", 1393409), ("Estados Unidos", 331002), ("Indonésia", 273523), ("Paquistão", 225199))
maisPop=max(paisesPop, key=lambda x: x[1])
print(maisPop)