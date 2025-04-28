descestu = 0.10
desccomp = 0.15
desc = 0
precio = input("ingrese el precio del artículo")
print("el precio del artículo es de ", precio)
r1 = input("¿es estudiante?")
r2 = input("¿es cliente frecuente?")
if r1 == "si":
    desc = descestu
elif r2 == "si":
    print
else:
print("usted no dispone de descuentos")