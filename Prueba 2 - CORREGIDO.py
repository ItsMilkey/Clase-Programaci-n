import os
import time
espaciador = "\n"+("*"*34)+"\n"
clean = "cls"
capacidad = 450
validar_name=False
Precio_servicio1 = 0
Total_Cilindro5 = 0
Precio_Cilindro5 = 0
Total_Cilindro15 = 0
Precio_Cilindro15 = 0
Total_Cilindro45 = 0
Precio_Cilindro45 = 0
SumaTotal = 0
PesoTotal = 0
os.system(clean)
while True:
    while True:
        try:
            name = input("Ingrese su nombre:\n").capitalize()
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
        print(f"El valor total hasta el momento es de: ${SumaTotal}")
        print(f"El peso total es de: {PesoTotal}kg")
        opc = int(input("Seleccione el producto que desee: "))
        if opc == 1:
            try:
                servicio1 = int(input("Indique la cantidad de camiones que necesite: "))
                if servicio1 >= 1:
                    Precio_servicio1 += (servicio1*765000)
                    SumaTotal += Precio_servicio1
                    PesoTotal += (450*servicio1)
                    os.system(clean)
                else:
                    print("No puedes ingresar valores negativos. ")
            except ValueError:
                print("Value error.")
        while opc == 2:
            os.system(clean)
            print("Productos específicos:\n1. Cilindro de 5kg $\n2. Cilindro de 15kg $ \n3. Cilindro de 45kg $\n4. Salir")
            a = int(input("Seleccione un producto específico: "))
            if a == 1:
                try:
                    os.system(clean)
                    a1 = int(input("Indique la cantidad de cilindros de 5kg: "))
                    Total_Cilindro5 += a1
                    Precio_Cilindro5 += (a1*9990)
                    PesoTotal += (5*a1)
                    SumaTotal+=Precio_Cilindro5
                    os.system(clean)
                except ValueError:
                    print("Value error. ")
            elif a == 2:
                try:
                    a2 = int(input("Indique la cantidad de cilindros de 15kg: "))
                    Total_Cilindro15 += a2
                    Precio_Cilindro15 += (a2*18990)
                    PesoTotal += (15*a2)
                    SumaTotal+=Precio_Cilindro15
                    os.system(clean)
                except ValueError:
                    print("Value error. ")
            elif a == 3:
                try:
                    a3 = int(input("Indique la cantidad de cilindros de 45kg: "))
                    Total_Cilindro45 += a3
                    Precio_Cilindro45 += (a3*27990)
                    PesoTotal += (45*a3)
                    SumaTotal+=Precio_Cilindro45
                    os.system(clean)
                except ValueError:
                    print("Value error. ")
                    time.sleep(2)
                    os.system(clean)
            elif a == 4:
                os.system(clean)
                print("Volviendo al menú principal.")
                time.sleep(2)
                os.system(clean)
                break
        if opc == 3:
            os.system(clean)
            print("Saliendo hacia la boleta.")
            time.sleep(2)
            os.system(clean)
            break
    #operaciones
    SumaTotal = SumaTotal
    cantidad_Camiones = round(PesoTotal/capacidad)
    print(f"{espaciador}\t\tBoleta{espaciador}\nCliente: {name}\nTeléfono: {telefono}\nCantidad de Kilos: {PesoTotal}\nCamiones: {cantidad_Camiones}\nValor Total: ${SumaTotal}{espaciador}")
    try:
        f= int(input("Desea realizar otro pedido?\n1 para sí\ncualquier otra tecla para no\n"))    
        if f==1:
            os.system(clean)
            print("Reiniciando sistema")
            time.sleep(2)
            capacidad = 450
            validar_name=False
            Precio_servicio1 = 0
            Total_Cilindro5 = 0
            Precio_Cilindro5 = 0
            Total_Cilindro15 = 0
            Precio_Cilindro15 = 0
            Total_Cilindro45 = 0
            Precio_Cilindro45 = 0
            SumaTotal = 0
            PesoTotal = 0
            True
            os.system(clean)
        else:
            print("Gracias por usar nuestro sistema.")
            break
    except ValueError:
        print("Ingresó un dato inválido, por favor Ingrese 1 o 2")