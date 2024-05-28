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
#
tot_servicio1 = 0
Total_Cilindro5 = 0
Total_Cilindro15 = 0
Precio_Cilindro15 = 0
Total_Cilindro45 = 0
Precio_Cilindro45 = 0

os.system(clean)
k=1
while k>=1:
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
        print(f"Menú de Servicios{espaciador}1. Entrega camión estándar. $765.000 por camión\n2. Carga específica\n3.Cerrar pedido (Imprimir boleta){espaciador}")
        opc = int(input("Seleccione el producto que desee: "))
        while opc == 1:
            try:
                servicio1 = int(input("Indique la cantidad de camiones que necesite: "))
                if servicio1 >= 1:
                    tot_servicio1 = (servicio1*765000)
                else:
                    print("No puedes ingresar valores negativos. ")
            except ValueError:
                print("Value error.")
        while opc == 2:
            print("Productos específicos:\n1. Cilindro de 5kg $\n2. Cilindro de 15kg $ \3. Cilindro de 45kg $")
            a = int(input("Seleccione un producto específico: "))
            if a == 1:
                try:
                    a1 = int(input("Indique la cantidad de cilindros de 5kg: "))
                    Total_Cilindro5 += a1
                    Precio_Cilindro5 = (a1*9990)
                except ValueError:
                    print("Value error. ")
            elif a == 2:
                try:
                    a2 = int(input("Indique la cantidad de cilindros de 15kg: "))
                    Total_Cilindro15 += a2
                    Precio_Cilindro15 = (a2*18990)
                except ValueError:
                    print("Value error. ")
            elif a == 3:
                try:
                    a3 = int(input("Indique la cantidad de cilindros de 45kg: "))
                    Total_Cilindro45 += a3
                    Precio_Cilindro45 = (a3*27990)
                except ValueError:
                    print("Value error. ")
        if opc == 3:
            break

#operaciones
SumaTotal = Precio_Cilindro5 + Precio_Cilindro15 + Precio_Cilindro45 + tot_servicio1
cantidad_Camiones = 




    print(f"{espaciador}Boleta\nCliente: {name}\nTeléfono: {telefono}\nCantidad de Kilos: {peso_servicio}\nCamiones: {camiones}\nValor Total: {valor_Total}{espaciador}")
    try:
        f= input("Desea realizar otro pedido?\n1 para sí\n2 para no")
        if f==2:
            k=0
            
        elif f==1:
            print("Reiniciando sistema")
            time.sleep(2)
            os.system(clean)
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
            k = 1
        else:
            print("Valor incorrecto")
    except ValueError:
        print("Ingresó un dato inválido, por favor Ingrese 1 o 2")
