
libros = [ 
"libro 1",
 "libro 2",
 "libro 3",
 "libro 4",
 "libro 5"
 ]
#perdon profe no me da para pensar en nombres de libros JNEFHJNFHWFBN


print("Bienvenido a tu biblioteca digital")

salir = True

while salir == True:

    print("\nElige una de las opciones")
    print("1. Ver todos los libros")
    print("2. Buscar un libro")
    print("3. Agregar un nuevo libro")
    print("4. Eliminar un libro")
    r = input("5. Salir\n")


    if r == "1":
        if len(libros) == 0:
                print("No hay libros")
        else:
            for i in libros:
                print(f"- {i}")
    elif r == "2":
        nombre = input("Ingresa el nombre del libro\n")
        if nombre in libros:
            print(f"El libro {nombre} se encuentra en tu biblioteca")
        else:
            print("El libro no se encuentra en tu biblioteca")
    elif r == "3":
        nlibro = input("Ingresa el nombre del libro que deseas agregar\n")
        if nlibro in libros:
            print("El libro ya existe en tu biblioteca")
        else:
            if len(libros) >= 10:
                print("Tu versión gratuita no admite agregar más de 10 libros en la biblioteca")
            else:
                libros.append(nlibro)
                print(f"El libro {nlibro} ha sido agregado a tu biblioteca")
    elif r == "4":
        eliminar = input("Ingrese el nombre del libro que desea eliminar de su biblioteca\n")
        if eliminar in libros:
            libros.remove(eliminar)
            print("El libro ha sido eliminado de su biblioteca")
        else:
            print(f"El libro {eliminar} no existe en su biblioteca")
    elif r == "5":
        print("Ha salido")
        salir = False
