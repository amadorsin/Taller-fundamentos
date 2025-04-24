palabra = ""
print("Ingrese una palabra")
palabra = input()
npalabra = ""


for i in range(len(palabra)):
    
    npalabra +=  palabra[(len(palabra) - 1) -i ]
    print("La nueva palabra es: " + npalabra)

if palabra == npalabra:
    print("La palabra ", palabra , "es palindromo")
else:
    print("La palabra ", palabra , "no es palindromo")