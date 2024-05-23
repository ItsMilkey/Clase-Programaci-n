matriz_sencilla = [
[1, 2, 3],
[4, 5, 6]
]
print("1) Imprimir matriz")
for i in matriz_sencilla:
    print(i)
print("2) Imprimir un elemento por posición")
print(matriz_sencilla[1][0])
print("3) Imprimir todos los elementos")
for fila in matriz_sencilla:
    for i in fila:
        print(i, end=' ')
print()

