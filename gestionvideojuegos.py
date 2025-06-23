listajuegos = []
ingresocodigo = False

def op1(nombrejuego, categoría, código):
    juego = {
        nombrejuego : {
            "categoría" : categoría,
            "código" : código	
        }
    }
    listajuegos.append(juego)
    return

def op2(nombre):
    return

def op3(nombre):
    eliminar = input("Ingrese el nombre del videojuego")
    return


while True:
    try:
        print("MENU PRINCIPAL")
        print("1.- Ingresar videojuego")
        print("2.- Buscar videojuegos")
        print("3.- Eliminar videojuego")
        print("4.- Salir")
        opcion = int(input())

        if opcion == 1:
            while True:
                nombrejuego = input("Ingrese el nombre del videojuego\n")
                if nombrejuego in listajuegos:
                    print("El juego ingresado ya existe")
                    print("Por favor, ingrese un juego no existente")
                else:
                    break

            while True:
                categoría = input("Ingrese la categoría del videojuego")
                if categoría != "A" and categoría != "I":
                    print("Debe ingresar 'A' (triple A) o 'I' (indie)")
                else:
                    break
                
            def codigovalido(código):
                while ingresocodigo == False:
                    código = input("Ingrese el código del videojuego")
                    if len(código) < 8:
                        print("El código debe contener al menos 8 caracteres")
                    elif len(código) > 8:
                        letras = False
                        numeros = False
                        espacios = False
                        for caracter in código:
                            if caracter.isalpha():
                                letras = True
                            elif caracter.isdigit():
                                numeros = True
                            elif caracter == " ":
                                print("El código no puede contener espacios")
                                espacios = True
                        if (letras and numeros == True) and (espacios == False):
                            print("Datos ingresados con éxito")
                            break
                        else:
                            print("El código debe tener al menos 1 letra y 1 número")
                            ingresocodigo = False


            op1(nombrejuego, categoría, código)
            

        elif opcion == 2:
            op2()
            
        elif opcion == 4:
            print("Ha salido")
            False

    except ValueError:
        print("Debe ingresar una opción válida")
        True