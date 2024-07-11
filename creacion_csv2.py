import csv
import os
import random

def datos():
    var1= 1
    var2 = 2
    var3 = random.randint(1,10)
    return var1, var2, var3

def crear(var1, var2, var3, archivo_csv = 'prueba3.csv'):
    try:
        with open(archivo_csv, 'a', newline='')as f:
            campos = ['VAR1', 'VAR2', 'VAR3']
            escritor = csv.DictWriter(f,fieldnames=campos)
            if f.tell()==0:
                escritor.writeheader()
            escritor.writerow({
                'VAR1':var1,
                'VAR2':var2,
                'VAR3':var3
            })
    except IOError:
        print("El archivo no se encuentra")

def leer(archivo_txt='prueba3.csv'):
    if os.path.exists(archivo_txt):
        with open(archivo_txt, 'r')as f:
            lector = csv.reader(f)
            for fila in lector:
                print(fila)

def principal():
    res = datos()
    if res:
        var1,var2,var3 = res
        crear(var1,var2,var3)
        leer()

principal()