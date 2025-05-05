#ej 1
user = "amador"
contraseña = "contraseña"
nuser = input("ingrese su nombre de usuario\n")
ncontraseña = input("ingrese su contraseña\n")
if user == nuser and contraseña == ncontraseña:
    print("ha iniciado sesion correctamente")
elif user == nuser and contraseña != ncontraseña:
    print("nombre de usuario correcto")
    print("contraseña incorrecta")
    print(f"su contraseña comineza con la letra {contraseña[0]}")
else:
    print("datos incorrectos")

