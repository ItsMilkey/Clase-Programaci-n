import csv
import os
import random
playlist = set()

def limpieza():
    clear = 'cls'
    os.system(clear)
def nro_serie():
    serie = random.randint(55555,9999999)
    return serie

Dic_Songs = {
    'Song':[]
}

def datos():
    name = input("Ingrese name: ").capitalize()
    song_name = input("Song Name: ").capitalize()
    song_artist = input("Artist: ").capitalize()
    song_lenght = input("Song Lenght: ")
    serie = nro_serie()
    # validad que todos los campos se hayan llenado correctamente
    if not name or not song_name or not song_artist or not song_lenght or not serie:
        print("Todos los campos son obligatorios")
        return None
    return name, song_name, song_artist, song_lenght, serie

# argumentos = variables retornadas en datos()
def registro(name,song_name,song_artist,song_lenght,serie,archivo_csv='playlist2.csv'):
    # 1) abrir el archivo
    with open(archivo_csv, 'a', newline='')as f:
        # 2) definir campos y header a la vez
        campos = ['Name', 'Song Name', 'Artist', 'Song Lenght', 'Serie']
        # 3) definir la variable escritor
        writer_csv = csv.DictWriter(f,fieldnames=campos)
        # 4) usar .tell, truquito para crear archivo si no está y luego escribir - clave
        if f.tell() == 0:
            writer_csv.writeheader()
        # 5) escribir en el diccionario asignando las variables existentes a los campos
        writer_csv.writerow({
            'Name':name,
            'Song Name':song_name,
            'Artist':song_artist,
            'Song Lenght':song_lenght,
            'Nroº Serie':serie
        })
        Dic_Songs[song_name].append((song_artist,serie))
        creartxt()

# argumento = archivo_csv
def mostrar(archivo_csv='playlist2.csv'):
    # 1) verificar que el archivo existe, así, si se usa la función en un menú se evitan errores de path finding
    #    importante importar os
    if os.path.exists(archivo_csv):
        # 2) abrir archivo
        with open(archivo_csv, 'r')as f:
            # 3) asignar la variable lector
            reader_csv = csv.reader(f)
            # 4) ciclo for para leer e imprimir las filas
            for fila in reader_csv:
                print(fila)
    else:
        print("El archivo .csv no existe.")

def eliminar_cancion(song_name, archivo_csv='playlist2.csv'):
    if os.path.exists(archivo_csv):
        with open(archivo_csv, 'r') as f:
            reader_csv = list(csv.DictReader(f))
        with open(archivo_csv, 'w', newline='') as f:
            campos = ['Name', 'Song Name', 'Artist', 'Song Lenght']
            writer_csv = csv.DictWriter(f, fieldnames=campos)
            writer_csv.writeheader()
            for row in reader_csv:
                if row['Song Name'] != song_name:
                    writer_csv.writerow(row)
            print(f"La canción '{song_name}' ha sido eliminada.")
    else:
        print("El archivo .csv no existe.")

def principal():
    limpieza()
    # 1) truquito, se llama a datos() y a la vez se asigna esta a la var resultado
    resultado = datos()
    # luego de la llamada:
    if resultado:
        # las variables retornadas se asignan a la var resultado (me imagino que es para convertirlas en variables locales y poder usarlas en la llamada de registro).
        name, song_name, song_artist, song_lenght, serie = resultado
        # se llama a registro, usando como argumento las variables retornadas asignadas a resultado
        registro(name,song_name,song_artist,song_lenght,serie)

def creartxt(archivo_txt='playlist_serial.txt'):
    with open(archivo_txt,'w')as f:
        for song_name,datos in Dic_Songs.items():
            archivo_txt.write(f"{song_name}:")
            for dato in datos:
                song_artist,serie = dato
                archivo_txt.write(f"    - Artist: {song_artist}, Nroº de serie: {serie}")
            archivo_txt.write("\n")

def leertxt(archivo_txt='playlist_serial.txt'): # Lee todo lo que hay dentro del txt
    if os.path.exists(archivo_txt):
        with open(archivo_txt,'r')as f:
            contenido = archivo_txt.read()
            print(f"Datos por canción:\n{contenido} ")
    else:
        print("El archivo txt no existe")

def leertxt_especifico(song_name,archivo_txt='playlist_serial.txt'): # Lee por canción especificada por usuario
    if os.path.exists(archivo_txt):
        with open(archivo_txt,'r')as f:
            lineas = f.readlines()
            for i in range(len(lineas)):
                if lineas[i].strip().startswith(song_name):
                    print(f"Datos de la canción {song_name}:")
                    j = i+1
                    while j < len(lineas) and lineas[j].strip().startswith("-"):
                        print(lineas[j].strip())
                        j += 1
                        break
                else:
                    print("El archivo no existe")
    else:
        print("El archivo txt no existe")

def menu_opc4():
    while True:
        try:
            opc = int(input("1) Ver datos de todas las canciones registradas\n2) Ver datos de canción específica"))
            if opc == 1:
                limpieza()
                leertxt()
                break
            elif opc == 2:
                while True:
                    limpieza()
                    song_name = input("Ingrese canción: ").capitalize()
                    if song_name not in Dic_Songs[song_name]:
                        print("La canción no se encuentra en los registros, intente nuevamente.\n")
                    else:
                        limpieza()
                        leertxt_especifico(song_name)
                        break
            else: 
                print("1-2")
        except ValueError:
            print("xd")


while True:
    print("Menú\n1. Añadir canción\n2. Mostrar playlist\n3. Eliminar canción\n4. Ver Nroº de serie\n5. Salir")
    try:
        opc = int(input("\nElija una opción: "))
        if opc == 1:
            principal()
        elif opc == 2:
            mostrar()
        elif opc == 3:
            song_name = input("\nIngrese la canción que desee eliminar: ").capitalize()
            eliminar_cancion(song_name)
        elif opc == 4:
            menu_opc4()
        elif opc == 5:
            break
        else:
            print("XD")
    except ValueError:
        print("Solo dígitos -db")


