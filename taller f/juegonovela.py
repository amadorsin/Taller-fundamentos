espada = 100
esatk = 50
arco = 90
arcatk = 60
lanza = 110
lanatk = 40
vida = 100
vidae1 = 100
from random import*

print("Bienvenido a tu nueva aventura")
print("En esta ocasión te enfrentarás a una guerra en donde tu deber es cortarle la cabeza al Rey")
print("Escoge tu arma")
print("1. Espada (vida 100) / atk 50")
print("2. Arco (vida 90) / atk 60")
print("3. Lanza (vida 110) / atk 40")

arma = input("Elige 1, 2 o 3")
if arma == "1":
    print("Haz elegido la Espada")
elif arma == "2":
    print("Haz elegido el Arco")
elif arma == "3":
    print("Haz elegido la Lanza")
    
print("¡Te haz lanzado a la guerra!")
print(f"Tu vida es de {vida}")

print("Te haz encontrado frente a tu primer oponente")
print(f"Su vida es de {vidae1}")


while vidae1 > 0:
    print("¿Qué acción realizarás?")
    print("1. Atacar")
    print("2. Evadir")
    respuesta = input("Elige 1 o 2")
    if respuesta == "1" and arma == "1":
        print("Haz atacado")
        esquivar = (randint(0,10))
        if esquivar > 8:
            print("El enemigo ha esquivado tu ataque")
        else:
            vidae1 = vidae1 - esatk
            print(f"Le haz inflingido {esatk} de daño")
            print(f"Ahora su vida es de {vidae1}")
            print("El enemigo te ha atacado")
            vida = vida - 20
            print (f"Ahora tu vida es de {vida}")
    elif respuesta == "1" and arma == "2":
        print("Haz atacado")
        esquivar = (randint(0,10))
        if esquivar > 8:
            print("El enemigo ha esquivado tu ataque")
        else:
            vidae1 = vidae1 - arcatk
            print(f"Le haz inflingido {arcatk} de daño")
            print(f"Ahora su vida es de {vidae1}")
            print("El enemigo te ha atacado")
            vida = vida - 20
            print (f"Ahora tu vida es de {vida}")
    elif respuesta == "1" and arma == "3":
        print("Haz atacado")
        esquivar = (randint(0,10))
        if esquivar > 8:
            print("El enemigo ha esquivado tu ataque")
        else:
            vidae1 = vidae1 - lanatk
            print(f"Le haz inflingido {lanatk} de daño")
            print(f"Ahora su vida es de {vidae1}")
            print("El enemigo te ha atacado")
            vida = vida - 20
            print (f"Ahora tu vida es de {vida}")
    elif respuesta == "2":
        
        print("Haz evadido")
