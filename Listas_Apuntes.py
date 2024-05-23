nombrelista = [1,2,3,4,5]
#Al igual que el FOR, se inica el recorrido desde la posición 0

#Recorre 1 a 1 los elementos dentro de la lista.
for i in nombrelista:
    print(i)
print("*"*34)
#Para buscar un elemento en una posición dentro de la lista. En este caso, busca la segunda posición en la lista, que sería el número 3.
print(nombrelista[2])

print("*"*34)
#Para añadir un nuevo elemento, usar: append()
nombrelista.append(6)
nombrelista.append(28)
nombrelista.append("roberto")
for elemento in nombrelista:
    print(elemento)
print("*"*34)
print(type(nombrelista))
print(nombrelista[7])
print("*"*34+"\n")

#Para agregar un nuevo elemento en una posición deseada, usar insert(), dentro especificar la posición y el dato a añadir:
#En este caso, la posición 4 la ocupa el 5, se desplaza hacia la derecha y ocupa el lugar
nombrelista.insert(4,"lobezno")
for i in nombrelista:
    print(i)
print("*"*34+"\n")

#
nombrelista.remove(28)
print(nombrelista)
print("*"*34+"\n")
#Para invertir el orden de los elementos de una lista, usar reverse()
#Para ordenar los elementos numéricos de menor a mayor, usar sort()

nombrelista.reverse()
print(nombrelista)
#nombrelista.sort()
#print(nombrelista)
