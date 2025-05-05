
print("te ayudo a deicidir si una canción es adecuada para tu playlist")
duracion = float(input("ingrese la duración de la canciónn\n"))
genero = input("ingrese el género de la canción\n").lower()
año = int(input("ingrese el año de lanzamiento de la canción\n"))
if duracion >= 2.5 and duracion <= 4.5:
    if genero == "rock" or "pop" or "indie":
        if año > 2010:
            print("la cancion es adecuada para tu playlist")
else:
    print("la canción no es adecuada")
