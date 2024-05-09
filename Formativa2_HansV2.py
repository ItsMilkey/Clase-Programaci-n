#Inicialización de variables.
import os
import time
clean = "cls"
descuento = "soyotaku"
descuento_Total= 0
total_Productos = 0
subTotal= 0
sumaTotal= 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4= 0
menuu=True
#menú
while True:
    while menuu==True:
        try:
            print('''\t1. Pikachu Roll $4500
            2. Otaku Roll $5000
            3. Pulpo Venenoso Roll $5200
            4. Anguila Eléctrica Roll $4800
            5. Continuar''')
            opc = int(input("Seleccione uno de los siguientes productos: "))
            if opc == 1:
                print("Has seleccionado Pikachu Roll. ")
                cont1 += 1
                subTotal = (subTotal+4500)
                os.system(clean)
            elif opc == 2:
                print("Ha seleccionado Otaku Roll. ")
                cont2 += 1
                subTotal = (subTotal+5000)
                os.system(clean)
            elif opc == 3:
                print("Ha seleccionado Pulpo Venenoso Roll.")
                cont3 += 1
                os.system(clean)
                subTotal = (subTotal+5200)
            elif opc == 4:
                print("Ha seleccionado Anguila Eléctrica Roll.")
                cont4 += 1
                subTotal = (subTotal+4800)
                os.system(clean)
            elif opc == 5:
                os.system(clean)
                break
            else:
                print("Valor inválido, intente seleccionar una opción nuevamente.")
                time.sleep(2)
                os.system(clean)
        except ValueError:
            print("Valor inválido, intente nuevamente. ")
    #Descuento
    while True:
        try:
            res=int(input("¿Quiere aplicar un código de descuento? 1 para Sí, 2 para No "))
            if res == 1:
                os.system(clean)
                desc=input("Ingrese su código de descuento: ")
                if desc==descuento:
                    descuento_Total = round(subTotal*0.1)
                    break
                elif desc!=descuento:
                    os.system(clean)
                    print("Código no válido\n*****************")
                    res2=input("¿Desea volver a ingresarlo?\n1 para volver a intentarlo.\nX en mayúsculas para continuar. ")
                    if res2==1:
                        os.system(clean)
                        res == 1
                    elif res2=="X":
                        os.system(clean)
                        break
            elif res == 2:
                os.system(clean)
                break
        except ValueError:
            print("Ingrese un valor correcto.")
    #Operaciones
    total_Productos = round(cont1+cont2+cont3+cont4)
    sumaTotal = round(subTotal-descuento_Total)
    #Boleta
    print("*"*30)
    print(f"TOTAL PRODUCTOS: {total_Productos}")
    print("*"*30)
    print(f'''\t1. Pikachu Roll: {cont1}
            2. Otaku Roll: {cont2}
            3. Pulpo Venenoso Roll: {cont3}
            4. Anguila Eléctrica Roll: {cont4}''')
    print("*"*30)
    print(f"Subtotal a pagar: {subTotal}\nDescuento por código: {descuento_Total}\nTotal: {sumaTotal}")
    repe=int(input("Presione 1 para volver a comprar.\nPresione 2 para salir del programa.\n "))
    if repe==1:
        os.system(clean)
        menuu==True
    elif repe==2:
        menuu==False
        break
