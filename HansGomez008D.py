import os
import time
espaciador = "\n"+("*"*34)+"\n"
clean = "cls"
cantidad_Kilos = 0
camiones = 0
camiones_servicio1 = 0
capacidad = 450
valor_Total= 0
valor_servicio1=0
validar_name=False
cant_cilindro5=0
cant_cilindro15=0
cant_cilindro45=0
multa1= 1700
peso_15=0
peso_45=0
peso_5=0
resto1=0
resto2=0
resto3=0

os.system(clean)

while True:
    try:
        name = input("Ingrese su nombre:\n ")
        longitud_name=len(name)
        if longitud_name>3:
            validar_name=True
            break
        else:
            print("Nombre inválido, ingrese un nombre mayor a 3 letras. ")
            time.sleep(2)
            validar_name=False
    except ValueError:
        print("Valores inválidos")
while validar_name==True:
    try:
        telefono = (input("Ingrese su número telefónico:\n"))
        longitud_telef=len(telefono)
        if longitud_telef<=9 and longitud_telef>=8:
            time.sleep(1)
            os.system(clean)
            break
        elif longitud_telef<8 or longitud_telef>9:
            print("Teléfono ingresado inválido.\n Intente nuevamente")
            time.sleep(2)
            os.system(clean)
        else:
            print("Caracteres inválidos, intente nuevamente.")
            time.sleep(2)
            os.system(clean)
    except ValueError:
        print("Ingrese valores correctos. ")

while True:
    try:
        print(f"Menú de Servicios{espaciador}1. Entrega camión estándar. $765.000 por camión\n2. Carga específica\n3.Cerrar pedido (Imprimir boleta){espaciador}")
        opc=int(input("Seleccione el producto que desee:\n"))
        if opc==1:
            os.system(clean)
            print(f"{espaciador}Ha seleccionado la opción 1. Entrega de camión estándar.\n")
            servicio1=int(input("Indique la cantidad de camiones que necesita: "))
            try:
                if servicio1>=1:
                    camiones_servicio1 = servicio1
                    peso_servicio1 = 450*camiones_servicio1
                    valor_servicio1 = (camiones_servicio1*765000)
                    print(f"¡Se han añadido {servicio1} camiones correctamente!\nVolviendo al menú{espaciador}")
                    time.sleep(2)
                    os.system(clean)
            except ValueError:
                print("Ingrese una cantidad válida.")
        elif opc==2:
            os.system(clean)
            print(f"Ha seleccionado la opción 2. Entrega de carga específica.\n")
            print(f"Tamaño de cilindros:{espaciador}1. Cilindro de 5 kilos\n2. Cilindro de 15 kilos\n3. Cilindro de 45 kilos.{espaciador}")
            try:
                
                servicio2=int(input("Seleccione los cilindros que necesite:\n"))
                if servicio2==1:
                    os.system(clean)
                    cant_cilindro5 = int(input("Indique la cantidad de cilindros de 5kg que desea: "))
                    peso_5=(cant_cilindro5*5)
                    resto1 = round(peso_5%capacidad)
                    print(f"¡Ha añadido {cant_cilindro5} cilindros de 5kg correctamente!")
                    time.sleep(1)
                    os.system(clean)
                elif servicio2==2:
                    cant_cilindro15 = int(input("Indique la cantidad de cilindros de 15kg que desea: "))                    
                    peso_15 = (cant_cilindro15*15)
                    resto2 = round(peso_15%capacidad)
                    print(f"¡Ha añadido {cant_cilindro15} cilindros de 15kg correctamente!")
                    time.sleep(1)
                    os.system(clean)
                elif servicio2==3:
                    cant_cilindro45 = int(input("Indique la cantidad de cilindros de 45kg que desea: "))
                    peso_45 = (cant_cilindro45*45)
                    resto3 = round(peso_45%capacidad)
                    print(f"¡Ha añadido {cant_cilindro45} cilindros de 45kg correctamente!")
                    time.sleep(1)
                    os.system(clean)
            except ValueError:
                print("Seleccione una opción válida. ")
        elif opc==3:
            os.system(clean)
            print(f"{espaciador}Saliendo del menú\n")
            time.sleep(2)
            os.system(clean)
            break
    except ValueError:
        print("Seleccione una opción válida.")
        time.sleep(2)
        os.system(clean)

peso_servicio = (peso_5 + peso_45) + peso_15 + (peso_servicio1)
camiones = round(peso_servicio/capacidad)
resto = round(resto1+resto2+resto3)
valor_del_resto = (resto*1700)+100000
if peso_servicio > capacidad:
    valor_Total = valor_del_resto+(765000*camiones)-765000+(valor_servicio1)
elif peso_servicio < capacidad:
    valor_Total=(peso_servicio*1700)+100000


print(f"{espaciador}Boleta\nCliente: {name}\nTeléfono: {telefono}\nCantidad de Kilos: {peso_servicio}\nCamiones: {camiones}\nValor Total: {valor_Total}{espaciador}")