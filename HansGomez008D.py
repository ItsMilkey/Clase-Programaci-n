import csv
import os
import random
import time
#saco5 = 0
#saco10 = 0
#saco20 = 0
#cantidad_5 = 0
#cantidad_10 = 0
#cantidad_20 = 0
dic_hojaruta = {
     'San Bernardo': [],
     'Calera de Tango': [],
     'Buin': []
}
def nro_random():
    nro_pedido = random.randint(1,1000)
    nro_pedido += 1
    return nro_pedido
def limpieza():
     time.sleep(0.5)
     clean = 'cls'
     os.system(clean)
def datos():
    cantidad_5 = 0
    cantidad_10 = 0
    cantidad_20 = 0
    nombre = input("Nombre: ").capitalize()
    apellido = input("Apellido: ").capitalize()
    direccion = input("Dirección: ").capitalize()
    while True:
        try:
            limpieza()
            sector_opc = int(input("Sector:\n1) San Bernardo 2)Calera de Tango 3) Buin"))
            if sector_opc == 1:
                sector = 'San Bernardo'
                break
            elif sector_opc == 2:
                sector = 'Calera de Tango'
                break
            elif sector_opc == 3:
                sector = 'Buin'
                break
            else:
                print("Elija opción entre 1-3")
        except ValueError:
            print("Ingrese solo valores numéricos.")
    while True:
            try:
                limpieza()
                saco_opc = int(input("Seleccione el producto que desee:\n1) Saco 5kg\n2) Saco 10kg\n3) Saco 20kg\n4) Continuar\n"))
                if saco_opc == 1:
                    try:
                        cantidad = int(input("Ingrese la cantidad deseada: "))
                        cantidad_5 += cantidad
                    except ValueError:
                        print("Dígitos solamente")
                elif saco_opc == 2:
                    try:
                        cantidad = int(input("Ingrese la cantidad deseada: "))
                        cantidad_10 += cantidad
                    except ValueError:
                        print("Dígitos solamente")
                elif saco_opc == 3:
                    try:
                        cantidad = int(input("Ingrese la cantidad deseada: "))
                        cantidad_20 += cantidad
                    except ValueError:
                        print("Dígitos solamente.")
                elif saco_opc == 4:
                    break                       
            except ValueError:
                 print("Sólo valores numéricos.")
    nro_pedido = nro_random()
    if not nombre or not apellido or not direccion or not sector:
         print("Los campos de nombre, apellido, dirección y sector son obligatorios.")
         return None
    print(f"Se ha añadido el pedido del cliente {nombre} {apellido}\nSe le asignó el Nroº de pedido: {nro_pedido}")
    return nombre, apellido, direccion, sector, cantidad_5, cantidad_10, cantidad_20, nro_pedido
                     
def registrar(nombre, apellido, direccion, sector, cantidad_5, cantidad_10, cantidad_20, nro_pedido, archivo_csv='Pedidos.csv'):
    with open(archivo_csv, 'a', newline='')as f:
        campos = ['Nro. Pedido', 'Cliente', 'Dirección', 'Sector', 'Saco 5kg', 'Saco 10kg', 'Saco 20kg']
        escritor = csv.DictWriter(f,fieldnames=campos)
        if f.tell()==0:
              escritor.writeheader()
        escritor.writerow({
             'Nro. Pedido': nro_pedido,
             'Cliente': nombre+apellido,
             'Dirección': direccion,
             'Sector': sector,
             'Saco 5kg': cantidad_5,
             'Saco 10kg': cantidad_10,
             'Saco 20kg': cantidad_20
        })
    dic_hojaruta[sector].append((nro_pedido,nombre+apellido,direccion,cantidad_5,cantidad_10,cantidad_20))
    #ruta_txt()

def listar_pedidos(archivo_csv='Pedidos.csv'):
    if os.path.exists(archivo_csv):
         with open(archivo_csv, 'r')as f:
              lector = csv.DictReader(f)
              for fila in lector:
                   print(fila)
    else:
         print("No se encuentra el archivo")

def ruta_txt(archivo_txt='Hoja_ruta.txt'): #no me acuerdo de como abrir txt
     with open(archivo_txt,'w')as f:
          #lineas = 
          #escritor_txt = (lineas)
         print("")
         
def leer_txt(archivo_txt='Hoja_ruta.txt'):
    if os.path.exists(archivo_txt):
        with open(archivo_txt, 'r') as f:
            #lector_txt = readlines(f)
            for sector, datos in dic_hojaruta.items():
               print(f"Hoja de ruta del sector {sector}:\n")
               nro_pedido,nombre,apellido,direccion,cantidad_5,cantidad_10,cantidad_20 = datos
               for dato in datos:
                    print(dato)
                    print(f"    -Nroº de Pedido: {nro_pedido}, Cliente: {nombre} {apellido}, Dirección: {direccion}\nSacos 5kg: {cantidad_5}, Sacos 10kg: {cantidad_10}, Sacos 20kg: {cantidad_20}\n")

def opcion1():
    limpieza()
    resultado = datos()
    if resultado:
        nro_pedido, nombre, apellido, direccion, sector, cantidad_5, cantidad_10,cantidad_20 = resultado
        registrar(nro_pedido, nombre, apellido, direccion, sector, cantidad_5, cantidad_10, cantidad_20)
def opcion3(archivo_csv='Pedidos.csv'):
    limpieza()
    if os.path.exists(archivo_csv):
        with open(archivo_csv, 'r')as f:
            lector = csv.DictReader(f)
            for fila in lector:
                print(fila)
    else:
        print("No se encuentra el archivo")


def menu_principal():
    while True:
        print("*************MENÚ PRINCIPAL*************\n1) Registrar pedido\n2) Listar todos los pedidos\n3) Imprimir hoja de ruta\n4) Salir del programa\n")
        try:
            opc = int(input("Seleccione un producto: "))
            if opc == 1:
                opcion1()
            elif opc == 2:
                limpieza()
                listar_pedidos()
            elif opc == 3:
                opcion3()
            elif opc == 4:
                print("Datos guardados\nSaliendo del programa")
                break
            else:
                print("Elija opción entre 1-4")
        except ValueError:
            print("Dato ingresado inválido, elija una opción correcta.")

menu_principal()
