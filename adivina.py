#adivinar un numero
import random

numero_secreto = random.randint(1, 10)
while(True):
    numero_usuario = int(input("Ingrese un numero entre 1 y 10: "))
    if numero_usuario == numero_secreto:
        print("¡Felicidades! Has acertado el numero secreto.")
        break
    elif numero_usuario < numero_secreto:
        print("El numero secreto es mayor que el que ingresaste. Intenta de veras")
    else:
        print("El numero secreto es menor que el que ingresaste. Intenta de veras")
        