notasAlunos = {'Alice': 8.5,'Bob': 7.2,'Carol': 9.0,'David': 6.8,'Eva': 9.5}
somaNotas=0
for x in notasAlunos.values():
    somaNotas+=x
media=somaNotas/len(notasAlunos)
print(media)