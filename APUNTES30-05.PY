#Diccionarios

diccionario_nombres = {'viccos' : '1234',
               'viccas' : '9876',
               'BasRoj' : '6543'}
usuario = ''
usuario = input("Ingrese el usuario que quiere buscar: ")
#Comparamos si lo encuentra
if diccionario_nombres.get(usuario, 'No existe')=='No existe':
    print("Usuario no existe")
else:
    print("Usuario existente")

#las tuplas almacenan datos que son inmutables
#puede contener el mismo elemento repetidas veces, para contar la cantidad de veces que esto ocurre, usar count()    
tupla = (1,2,4,1,5,7,1,2)
print(tupla.count(1))

#Para saber la posición de un dato dentro de la tupla:
tupla.index(5)
#el elemento 5 está en la posición 5 de la tupla
