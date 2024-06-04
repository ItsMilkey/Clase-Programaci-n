Cant_Veh = 0
Capacidad = 4
Valor_Total = 0
resto = 0
sobrante2 = 0
ciclo = True
while ciclo==True:
    Cant_Personas = int(input("Ingrese la cantidad de personas: "))
    while True:
        try:
            if Cant_Personas == 4:
                Cant_Veh = round(Cant_Personas/Capacidad)
                Valor_Total += 150000
                break
            elif Cant_Personas<4:
                Cant_Veh = 1
                Valor_Total += round(Cant_Personas*35000)+50000
                break
            elif Cant_Personas > 4:
                Cant_Veh = round(Cant_Personas/Capacidad)
                resto = round(Cant_Personas%Capacidad)
                Valor_Total += (150000 * Cant_Veh)
                if resto>=1 or resto!=0:
                    Valor_Total += (resto*35000)+50000-150000
                break       
        except ValueError:       
                print("Datos ingresados inválidos. Inténtelo nuevamente. ")
    print(f'''Empresa de transportes LU
        Cantidad de vehículos a usar: {Cant_Veh}
        Cantidad de personas: {Cant_Personas} 
        Valor a pagar: {Valor_Total}''')
    try: 
        reinicio = int(input("Presione 1 para reiniciar sistema, 2 para salir."))
        if reinicio==1:
            print("reiniciando sistema. ")
            Cant_Veh = 0
            Capacidad = 4
            Valor_Total = 0
            resto = 0
            sobrante2 = 0
            ciclo=True
        elif reinicio==2:
            ciclo==False
            break
        else:
            print("error aaaaaaaaaaaaaaa")
    except ValueError:
        print("xd")