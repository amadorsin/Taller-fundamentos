num1 = 2
num2 = 1
vida = 3
while num1 > num2:
    num1 = int(input("Ingrese el primer número\n"))
    num2 = int(input("Ingrese el segundo número (Mayor que el primer número)\n"))
    if num1 > num2:
        print("El primer número no puede ser mayor que el segundo")

puntomedio = (num1 + num2) / 2
ajustealea = (num2 - num1) * 0.2

numalea = puntomedio + ajustealea


adivinar = int(input("Por favor, intente adivinar el número aleatorio"))
if adivinar == numalea:
    print("!Haz adivinado¡")
else:
    print("Haz perdido una oportunidad")
    print(f"Te quedan {vida} intentos")
    if adivinar > numalea:
        print("El número que ingresaste es mayor que el número aleatorio")
    elif adivinar < numalea:
        print("El número que ingresaste es menor que el número aleatorio")
    adivinar2 = int(input("Por favor, intente adivinar el número aleatorio"))
    if adivinar2 == numalea:
        print("!Haz adivinado¡")
    else:
        print("")