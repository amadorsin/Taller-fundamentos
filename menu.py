numeros = []
menu = True
ingresar_numero = False

while menu == True:
    try:
        print("***MENU PRINCIPAL***")
        print("1.- Ingresar número")
        print("2.- Mostrar mayor")
        print("3.- Mostrar menor")
        print("4.- Salir")
        opcion = int(input())
        menu = False
    except ValueError:
        print("Debe ingresar una opción válida")
        menu = True

if opcion == 1:
    while ingresar_numero == False:
        try:
            numero = int(input("Ingrese un número entre 0 y 100\n"))
            if numero < 0 or numero > 100:
                print("Debe ingresar un número dentro del rango")
                ingresar_numero = False
            else:
                numeros.append(numero)
                print("Ingreso exitoso")
                ingresar_numero = True
        except ValueError:
            print("Debe ingresar un número entero")
            ingresar_numero = False
