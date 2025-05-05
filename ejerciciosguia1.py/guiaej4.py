k = 0
r = 0

print("1. Convertir de kilómetros a millas")
print("2. Convertir de millas a kilómetros")
print("3. Convertir de grados Celsius a Fahrenheit")
print("4. Convertir de grados Fahrenheit a Celsius")
respuesta = input("Elija una de las opciones\n")

if respuesta == "1":
    k = float(input("Ingrese los kilómetros\n"))
    if k < 0:
        print("Datos ingresados inválidos, los kilómetros no pueden ser negativos")
    else:
        r = k * 0.621371
        print(f"Los kilómetros ingresados convertidos a millas serían: {r:.2f} millas")
elif respuesta == "2":
    k = float(input("Ingrese las millas\n"))
    if k < 0:
        print("Datos ingresados inválidos, las millas no pueden ser negativas")
    else:
        r = k / 0.621371
        print(f"Las millas convertidas a kilómetros serían: {r:.2f} kilómetros")
elif respuesta == "3":
    k = float(input("Ingrese los grados celsius\n"))
    r = k * 9 / 5 + 32
    print(f"Los grados celsius ingresados convertidos a grados fahrenheit serían: {r:.1f} grados fahrenheit")
    if k < 0:
        print("La temperatura está bajo cero")
    elif k <=25 and r >=15:
        print("La temperatura está a temperatura ambiente")
    elif k > 25:
        print("La temperatura está calurosa")
elif respuesta == "4":
    k = float(input("Ingrese los grados fahrenheit\n"))
    r = (k - 32) * 5/9
    print(f"Los grados fahrenheit ingresados convertidos a grados celsius serían: {r:.1f} grados celisus")
    if r < 0:
        print("La temperatura está bajo cero")
    elif r <=25 and r >=15:
        print("La temperatura está a temperatura ambiente")
    elif r > 25:
        print("La temperatura está calurosa")
else:
    print("Opción ingresada inválida")