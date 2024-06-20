import csv
import os
limpiarPantalla = "cls"
minuscula = 0
matrizFruta = []
listaFruta = []
opMenu = True

while opMenu == True:
    os.system(limpiarPantalla)
    print("********** MENU MANTENEDOR DE FRUTA **********")
    print("1. Ingresar fruta") # Creaciòn de un dato a la lista
    print("2. Consulta") # Consulta que datos hay dentro de la matriz
    print("3. Añadir fruta") # Agrega un nuevo dato a una matriz
    print("4. Carga de datos") # (try) fruta.append = [nombre, unidad, cantidad, precio] / [pera, kilo, 10, 1500]
    print("5. Guardado") # Guarda los datos a una matriz
    print("6. Salida del sistema")
    
    try:
        respuestaOp = int(input("\nIngrese su opciòn del menù: "))
    except ValueError:
        print("El valor ingresado no es correcto")
    if opMenu == 1:
        print("********** INGRESO DE FRUTAS **********")
        ingresoFruta = str(input("Ingrese el nombre de la fruta que desea ingresar: "))
        minuscula = ingresoFruta.lower()
        listaFruta.append(minuscula)
        opMenu = False
        
    elif opMenu == 2:
        if len(listaFruta) == 0:
            print("No hay datos por mostrar")
        else:
            print(listaFruta)
        opMenu = False