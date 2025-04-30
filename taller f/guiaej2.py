descestu = 0.10
desccomp = 0.15
desc = 0.0
precio = float(input("ingrese el precio del artículo\n"))
print("el precio del artículo es de ", precio)
r1 = input("¿es estudiante? (si/no)")
r2 = input("¿es cliente frecuente? (si/no)")
if r1 == "si" and r2 == "si":
    desc = desccomp
    precion = precio * desc
    preciodesc = precio - precion
    print("el precio final de su artículo con descuento es de ", preciodesc)
elif r1 == "si" and r2 == "no":
    desc = descestu
    precion = precio * desc
    preciodesc = precio - precion
    print("el precio final de su artículo con descuento es de ", preciodesc)
elif r1 == "no" and r2 == "si":
    desc = desccomp
    precion = precio * desc
    preciodesc = precio - precion
    print("el precio final de su artículo con descuento es de ", preciodesc)
elif r1 == "no" and r2 == "no":
    print("usted no dispone de descuentos")
