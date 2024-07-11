import csv
import random
import os
import time

def limpieza():
    clean = 'cls'
    os.system(clean)
    time.sleep(0.5)

def nro_random():
    nro_pedido_base = random.randint(1,1000)
    nuevo_numero = nro_pedido_base +1
    return nuevo_numero

rutadicc = {
    'San Bernardo': [],
    'Buin': [],
    'Calera de Tango': []
}

# sección csv
def datos():
    limpieza()
    saco5 = 0
    saco10 = 0
    saco20 = 0
    name = input("Nombre: ")
    apellido = input("Apellido: ")
    direccion = input("Dirección: ")
    while True:
        try:
            limpieza()
            sector = int(input("Seleccione sector: \n1) San Bernardo\n2) Buin\n3) Calera de Tango\n"))
            if sector == 1:
                sector = 'San Bernardo'
                break
            elif sector == 2:
                sector = 'Buin'
                break
            elif sector == 3:
                sector = 'Calera de Tango'
                break
            else:
                print("Seleccione entre 1-3")
        except ValueError:
            print("Dato ingresado inválido, intente nuevamente.")
    while True:
        try:
            limpieza()
            saco = int(input("Seleccione producto:\n1) Saco 5kg\n2) Saco 10kg\n3) Saco 20kg\n4) Continuar"))
            if saco == 1:
                try:
                    cantidad = int(input("Ingrese la cantidad de sacos de 5kg que desee en dígitos: "))
                    saco5 += cantidad
                except ValueError:
                    print("Sólo dígitos.")
            elif saco == 2:
                try:
                    cantidad = int(input("Ingrese la cantidad de sacos de 10kg que desee en dígitos: "))
                    saco10 += cantidad
                except ValueError:
                    print("Solo dígitos")
            elif saco == 3:
                try:
                    cantidad = int(input("Ingrese la cantidad de sacos de 20kg que desee en dígitos: "))
                    saco20 += cantidad
                except ValueError:
                    print("solo dígitos")
            elif saco == 4:
                break
            else:
                print("elija entre opciones 1-3")
        except ValueError:
            print("Dato ingresado inválido, intente nuevamente.")
    nro_pedido = nro_random()
    if not name or not apellido or not direccion or not sector:
        return None
    return name,apellido,direccion,sector,saco5,saco10,saco20,nro_pedido

def registro_csv(name,apellido,direccion,sector,saco5,saco10,saco20,nro_pedido,archivo_csv='Sumativa3RE.csv'):
    with open(archivo_csv,'a',newline='')as f:
        campos = ['Nroº Pedido','Cliente','Dirección','Sector','Saco 5kg','Saco 10kg','Saco 20kg']
        escritor_csv = csv.DictWriter(f,fieldnames=campos)
        if f.tell() == 0:
            escritor_csv.writeheader()
        escritor_csv.writerow({
            'Nroº Pedido':nro_pedido,
            'Cliente':name+apellido,
            'Dirección':direccion,
            'Sector':sector,
            'Saco 5kg':saco5,
            'Saco 10kg':saco10,
            'Saco 20kg':saco20
        })
    rutadicc[sector].append((name+apellido,direccion,saco5,saco10,saco20,nro_pedido))

def mostrar_csv(archivo_csv='Sumativa3RE.csv'):
    try:
        if os.path.exists(archivo_csv):
            with open(archivo_csv, 'r')as f:
                lector_csv = csv.reader(f)
                for fila in lector_csv:
                    print(fila)
        else:
            print("No existe el archivo")
    except IOError:
        print("El archivo no existeeee")

def opcion1():
    res = datos()
    if res:
        name,apellido,direccion,sector,saco5,saco10,saco20,nro_pedido = res
        registro_csv(name,apellido,direccion,sector,saco5,saco10,saco20,nro_pedido)
        print(f"Se registró correctamente al cliente {name} {apellido} y se le asignó el nro pedido {nro_pedido}")

# sección txt
def almacenar_en_txt(sector, archivo_txt = 'rutaa.txt'):
    with open(archivo_txt, 'w')as f:
        f.write(f"{sector}: \n")
        f.write("Cliente - Dirección - Saco 5kg - Saco 10kg - Saco 20kg - Nroº Pedido\n")
        for dato in rutadicc[sector]:
            f.write(f"  - {dato}\n")

def leer_txt(archivo_txt='rutaa.txt'):
    with open(archivo_txt,'r')as f:
        contenido = f.read()
        print(contenido)

def ruta(sector,archivo_txt='rutaa.txt'):
    with open(archivo_txt,'r')as f:
        almacenar_en_txt(sector,archivo_txt)
        leer_txt(archivo_txt)

while True:
    try:
        opc = int(input("1) registrar\n2) ver pedidos\n3) ver hoja de ruta\n4) salir"))
        if opc == 1:
            opcion1()
        elif opc == 2:
            limpieza()
            mostrar_csv()
        elif opc == 3:
            while True:
                try:
                    seleccion = int(input("Seleccione el sector para imprimir hoja de ruta:\n1) San bernardo\n2) Buin\n3) Calera de Tango\n"))
                    if seleccion == 1:
                        ruta('San Bernardo')
                    elif seleccion == 2:
                        ruta('Buin')
                    elif seleccion == 3:
                        ruta('Calera de Tango')
                    elif seleccion == 4:
                        break
                    else:
                        print("1-3")
                except ValueError:
                    print("aaaaaaaaaaaaaaaaaa")
        elif opc == 4:
            break
        else:
            print("xd")
    except ValueError:
        print("locura")



        