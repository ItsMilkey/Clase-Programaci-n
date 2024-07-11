import csv
import os
import time
from math import prod

def limpieza():
    cls="cls"
    os.system(cls)
    time.sleep(0.5)
# Diccionario para almacenar cargos y posteriormente añadir al .txt
sueldos_por_cargo = {
    "CEO": [],
    "Desarrollador": [],
    "Analista de datos": []
}

# 1) Pedir datos
def datos():
    nombre=input("Nombre y apellido del trabajador: ")
    while True:
        limpieza()
        print("Seleccione un cargo\n1. CEO\n2. Desarrollador\n3. Analista de datos\n")
        try:
            seleccion_cargo=int(input("Cargo del trabajador: "))
            if seleccion_cargo==1:
                cargo = 'CEO'
                break
            elif seleccion_cargo==2:
                cargo = 'Desarrollador'
                break
            elif seleccion_cargo == 3:
                cargo = 'Analista de datos'
                break
            else:
                limpieza()
                print("Cargo no existe, seleccione uno existente.")
        except ValueError:
            print("Seleccione usando dígitos.")
    try:
        sueldo_bruto=int(input("Sueldo bruto: "))
    except ValueError:
        print("Solo valores númericos permitidos.")
        return None
    des_salud = (sueldo_bruto * 0.07)
    des_afp = (sueldo_bruto * 0.1)
    liquido = sueldo_bruto - (des_salud+des_afp)
    return nombre, cargo, sueldo_bruto, des_salud, des_afp, liquido

# 2) Registrar datos en un .csv
def archivo_registro_csv(nombre, cargo, sueldo_bruto,des_salud,des_afp,liquido, archivo_csv= 'Planilla.csv'):
    with open(archivo_csv, 'a', newline='') as archivo:
        campos=['Nombre','Cargo','Sueldo Bruto','Desc. Salud','Desc. AFP','Sueldo Líquido']
        escritor_csv=csv.DictWriter(archivo,fieldnames=campos)
        if archivo.tell() == 0:
            escritor_csv.writeheader()
        escritor_csv.writerow({
            'Nombre': nombre,
            'Cargo': cargo,
            'Sueldo Bruto': sueldo_bruto,
            'Desc. Salud':des_salud,
            'Desc. AFP':des_afp,
            'Sueldo Líquido':liquido
        })
    sueldos_por_cargo[cargo].append((nombre,sueldo_bruto,des_salud,des_afp,liquido))
    guardar_sueldos_cargos()

# Leer .csv
def mostrar_contenido_csv(archivo_csv='Planilla.csv'):
    if os.path.exists(archivo_csv):
        with open(archivo_csv, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            for fila in lector_csv:
                print(fila)
    else:
        print("El archivo Planilla.csv no existe.")

# Para guardar datos en el txt
def guardar_sueldos_cargos(archivo_txt='sueldos_cargos.txt'):
    with open(archivo_txt, 'w') as archivo:
        for cargo, sueldos in sueldos_por_cargo.items():
            archivo.write(f"{cargo}:\n")
            for sueldo in sueldos:
                nombre, sueldo_bruto, des_salud, des_afp, liquido = sueldo
                archivo.write(f"  - Nombre: {nombre}, Sueldo Bruto: {sueldo_bruto}, Desc. Salud: {des_salud}, Desc. AFP: {des_afp}, Sueldo Líquido: {liquido}\n")
            archivo.write("\n")

# Para la opción 3-1 (Mostrar todos los datos por cargo existente en la planilla)
def mostrar_sueldos_cargos(archivo_txt='sueldos_cargos.txt'):
    if os.path.exists(archivo_txt):
        with open(archivo_txt, 'r') as archivo:
            contenido = archivo.read()
            print("Sueldos por cargo:")
            print(contenido)
    else:
        print("El archivo sueldos_cargos.txt no existe.")

# Para leer específicamente los datos según cargo especificado por usuario dentro del .txt (se llama en el menú dentro de
# la siguiente función "mostrar_sueldos_por_cargo" 
def leer_txt(cargo,archivo_txt='sueldos_cargos.txt'):
    with open(archivo_txt, 'r')as f:
        lineas = f.readlines()
        for i in range(len(lineas)):
            if lineas[i].strip().startswith(cargo):
                print(f"Sueldos para el cargo {cargo}:")
                j = i+1
                while j < len(lineas) and lineas[j].strip().startswith('-'):
                    print(lineas[j].strip())
                    j += 1
                break
            else:
                print("El archivo .txt no existe.")

# Para la opción 3-2 (Mostrar sueldos por cargo especificado por usuario)
def mostrar_sueldos_por_cargo(archivo_txt='sueldos_cargos.txt'):
    if os.path.exists(archivo_txt):
        while True:
            try:
                cargo= int(input("Ingrese el cargo para mostrar los sueldos:\n1. CEO\n2. Desarrollador\n3. Analista de datos\n4.Salir\n "))
                if cargo == 1:
                    limpieza()
                    # se llama a la función utilizando como argumento el string asociado a la key dentro del diccionario
                    leer_txt('CEO')
                    break
                elif cargo == 2:
                    limpieza()
                    leer_txt('Desarrollador')
                    break
                elif cargo == 3:
                    limpieza()
                    leer_txt('Analista de datos')
                    break
                elif cargo == 4:
                    break
                else:
                    limpieza()
                    print("Seleccione una de las opciones disponibles.")
            except ValueError:
                limpieza()
                print("Solo dígitos.")

def principal():
    resultado = datos()
    if resultado:
        nombre, cargo, sueldo_bruto, des_salud, des_afp, liquido = resultado
        limpieza()
        archivo_registro_csv(nombre, cargo, sueldo_bruto, des_salud, des_afp, liquido)
        limpieza()
        print(f"Se ha registrado correctamente al trabajador {nombre}")  

def calcular_media_geometrica(sueldos):
    if len(sueldos) == 0:
        return None
    producto = prod(sueldos)
    return producto ** (1 / len(sueldos))

def mostrar_media_geometrica():
    for cargo, sueldos in sueldos_por_cargo.items():
        sueldos_liquidos = [sueldo[4] for sueldo in sueldos]
        media_geom = calcular_media_geometrica(sueldos_liquidos)
        if media_geom:
            print(f"La media geométrica de los sueldos líquidos para {cargo} es: {media_geom:.2f}")
        else:
            print(f"No hay sueldos registrados para {cargo}")

def menu_principal():   
    while True:
        print("1. Registrar trabajador\n2. Listar todos los trabajadores\n3. Imprimir planilla de sueldos\n4. Media geométrica\n5. Salir del programa")
        try:
            opc = int(input("Seleccione la opción que desee: "))
            if opc == 1:
                limpieza()
                principal()
            elif opc == 2:
                limpieza()
                mostrar_contenido_csv()
            elif opc == 3:
                try:
                    limpieza()
                    opc2=int(input("1. Mostrar planilla de sueldos\n2. Mostrar planilla de sueldos por cargo específico\n"))
                    if opc2 == 1:
                        limpieza()
                        mostrar_sueldos_cargos()
                    elif opc2 == 2:
                        limpieza()
                        mostrar_sueldos_por_cargo()
                    else:
                        limpieza()
                        print("Inválido, ingrese una opción correcta.")
                except ValueError:
                    print("Ingrese solo dígitos.")
            elif opc == 4:
                limpieza()
                mostrar_media_geometrica()
            elif opc == 5:
                "Saliendo del programa"
                limpieza()
                break
            else:
                print("Me vuelvo loco")
        except ValueError:
            print("Opción inválida, ingrese una opción correcta. ")

menu_principal()
