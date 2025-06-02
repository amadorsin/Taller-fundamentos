noprimo = 0
primo = 0
ciclo = True
ciclo1 = True
divisores = []

while ciclo1 == True:
    try:
        cantidad = int(input("Ingresa la cantidad de números a verificar\n"))
        if cantidad < 1:
            print("Debe ingresar un número entero")
            ciclo1 = True
        else:
            ciclo1 = False
            
    except ValueError:
        print("Debe ser un numero entero")

while ciclo:
    try:
        for numeros in range(cantidad):
        
            numero = int(input("Ingrese número\n"))
            if numero == 2:
                print("Es primo")
                primo = primo +1
            else:
                for i in range(1, numero + 1):  
                    divisor = i
                    resultado = numero / divisor
                    
                    if numero % divisor == 0:
                        divisores.append(divisor)
                if len(divisores) == 2:
                    print(f"{numero} Es primo")
                    primo = primo +1
                else:
                    print(f"{numero} No es primo")
                    noprimo = noprimo +1
        
        print(f"La cantidad de números primos es: {primo}")
        print(f"La cantidad de números no primos es: {noprimo}")
        ciclo = False

    except ValueError:
            print("Debe ingresar un número entero")
            print(f"Vamos de nuevo, ingrese los {cantidad} números")
            primo = 0
            noprimo = 0
            ciclo = True